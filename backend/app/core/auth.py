import jwt
from functools import wraps
from flask import abort, current_app, g, request

from app.extensions import db
from app.modules.identity.models import User


def authenticate_request():
    """
    LÓGICA: Middleware de Autenticação JWT.
    Extrai o token Bearer, decodifica via SECRET_KEY e injeta o modelo User no contexto (g.user).
    Falhas resultam em g.user = None, delegando a recusa para o decorator de autorização.
    """
    g.user = None
    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        return

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id:
            g.user = db.session.get(User, user_id)
    except jwt.ExpiredSignatureError:
        current_app.logger.warning("Tentativa de acesso com token JWT expirado.")
    except jwt.InvalidTokenError:
        current_app.logger.warning("Tentativa de acesso com token JWT inválido.")


def requires_permission(permission_name: str):
    """
    LÓGICA: Decorator RBAC (Role-Based Access Control).
    Garante que o ator logado no contexto atual (`g.user`) possua a permissão
    sistêmica exigida através das Roles associadas.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = getattr(g, "user", None)
            
            # 1. Validação de Identidade (Autenticação)
            if not user:
                current_app.logger.warning(
                    f"Acesso negado: Tentativa anônima de acessar rota protegida ({permission_name})."
                )
                abort(401, description="Autenticação requerida.")

            # 2. Travessia do Grafo de Autorização
            has_permission = any(
                perm.name == permission_name 
                for role in user.roles 
                for perm in role.permissions
            )
            
            if not has_permission:
                current_app.logger.warning(f"Acesso negado: Usuário '{user.id}' não possui '{permission_name}'.")
                abort(403, description=f"Privilégios insuficientes. Necessário: {permission_name}")

            return f(*args, **kwargs)
        return decorated_function
    return decorator