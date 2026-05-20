import sys
from pathlib import Path

# Adiciona a raiz do backend ao PYTHONPATH para importar os módulos da aplicação
backend_dir = Path(__file__).resolve().parents[3]
if str(backend_dir) not in sys.path:
    sys.path.append(str(backend_dir))

from flask import current_app
from app import create_app
from app.extensions import db
from app.modules.organizations.models import Organization
from app.modules.identity.models import Permission, Role, User


def run_seed():
    app = current_app._get_current_object() if current_app else create_app()
    
    with app.app_context():
        print("==> Iniciando seed fundacional (Fase 1: v0.2.0-alpha)...")
        
        # 1. GRAMÁTICA: Definição de Permissões Base (Alinhadas ao Anti-escopo)
        permissions_data = [
            {"name": "system:admin", "description": "Acesso total de configuração sistêmica"},
            {"name": "audit:read", "description": "Leitura de trilhas imutáveis de auditoria"},
            {"name": "reconciliation:run", "description": "Executar motor de reconciliação informacional"},
            {"name": "reconciliation:read", "description": "Visualizar findings e anomalias de reconciliação"},
            {"name": "evidence:upload", "description": "Fazer upload de documentos com hash para o cofre"},
        ]

        perms_map = {}
        for p_data in permissions_data:
            perm = Permission.query.filter_by(name=p_data["name"]).first()
            if not perm:
                perm = Permission(name=p_data["name"], description=p_data["description"])
                db.session.add(perm)
                print(f"  [+] Permissão criada: {p_data['name']}")
            perms_map[p_data["name"]] = perm

        # 2. GRAMÁTICA: Tenant Foundation (Organização Raiz)
        org_name = "CoinBalance Foundation"
        org = Organization.query.filter_by(legal_name=org_name).first()
        if not org:
            org = Organization(legal_name=org_name, display_name="CoinBalance Global")
            db.session.add(org)
            db.session.flush()  # Garante a alocação do ID no banco
            print(f"  [+] Organização criada: {org.display_name} ({org.id})")
        else:
            print(f"  [=] Organização já existente: {org.display_name}")

        # 3. LÓGICA: Roles e Associação com Permissões
        roles_data = [
            {
                "name": "System Administrator",
                "description": "Administrador Global",
                "permissions": ["system:admin", "audit:read", "reconciliation:run", "reconciliation:read", "evidence:upload"],
                "is_global": True,  # Role de sistema (organization_id = None)
            },
            {
                "name": "Auditor",
                "description": "Auditor independente focado em trilhas",
                "permissions": ["audit:read", "reconciliation:read"],
                "is_global": False,  # Atrelado a uma org específica
            },
        ]

        for r_data in roles_data:
            org_id = None if r_data.get("is_global") else org.id
            role = Role.query.filter_by(name=r_data["name"], organization_id=org_id).first()
            if not role:
                role = Role(name=r_data["name"], description=r_data["description"], organization_id=org_id)
                for p_name in r_data["permissions"]:
                    role.permissions.append(perms_map[p_name])
                db.session.add(role)
                print(f"  [+] Role criada: {r_data['name']}")

        db.session.commit()
        print("==> Seed concluído com sucesso e transação validada.")


if __name__ == "__main__":
    run_seed()
