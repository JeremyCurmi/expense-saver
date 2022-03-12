import logging
from sqlalchemy.orm import Session
from app.crud import AccountCrud, UserCrud, RoleCrud, UserRoleCrud
from app.core import settings
from app import schemas, models
from app.constants.role import Role

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_initial_super_admin_account(db: Session):
    logging.info("Creating super admin account 🚀")
    account = AccountCrud(db).get_by_name(settings.OWNER_ACCOUNT_NAME)
    if not account:
        logging.info("Creating Owner account 🚀")
        new_account = schemas.AccountCreate(
            name = settings.OWNER_ACCOUNT_NAME,
            description="super admin account",
        )
        AccountCrud(db).create(new_account)

def create_initial_super_admin_user(db: Session) -> models.User:
    logging.info("Creating super admin user 🚀")
    user = UserCrud(db).get_by_email(settings.OWNER_EMAIL)
    if not user:
        account = AccountCrud(db).get_by_name(settings.OWNER_ACCOUNT_NAME)
        new_user = schemas.UserCreate(
            full_name=settings.OWNER_ACCOUNT_NAME,
            phone_number=settings.OWNER_PHONE_NUMBER,
            email=settings.OWNER_EMAIL,
            account_id = account.id,
            password=settings.OWNER_PASSWORD
        )
        user = UserCrud(db).create(new_user)
    return user


def create_roles(db: Session) -> None:
    logging.info("Creating roles 🚀")
    guest_role = RoleCrud(db).get_by_name(Role.GUEST["name"])
    if not guest_role:
        RoleCrud(db).create(schemas.RoleCreate(name=Role.GUEST["name"],
                                               description=Role.GUEST["description"]))

    account_admin_role  = RoleCrud(db).get_by_name(Role.ACCOUNT_ADMIN["name"])
    if not account_admin_role:
        RoleCrud(db).create(schemas.RoleCreate(name=Role.ACCOUNT_ADMIN["name"],
                                               description=Role.ACCOUNT_ADMIN["description"]))

    account_manager_role = RoleCrud(db).get_by_name(Role.ACCOUNT_MANAGER["name"])
    if not account_manager_role:
        RoleCrud(db).create(schemas.RoleCreate(name=Role.ACCOUNT_MANAGER["name"],
                                               description=Role.ACCOUNT_MANAGER["description"]))

    admin_role   = RoleCrud(db).get_by_name(Role.ADMIN ["name"])
    if not admin_role :
        RoleCrud(db).create(schemas.RoleCreate(name=Role.ADMIN["name"],
                                               description=Role.ADMIN["description"]))

    super_admin_role  = RoleCrud(db).get_by_name(Role.SUPER_ADMIN["name"])
    if not super_admin_role :
        RoleCrud(db).create(schemas.RoleCreate(name=Role.SUPER_ADMIN["name"],
                                               description=Role.SUPER_ADMIN["description"]))


def set_super_admin_role_to_user(db: Session, user: models.User):
    logging.info("Setting user role for super admin 🚀")
    user_role = UserRoleCrud(db).get_by_id(user.id)
    if not user_role:
        role = RoleCrud(db).get_by_name(name=Role.SUPER_ADMIN["name"])
        user_role_in = schemas.UserRoleCreate(user_id=user.id, role_id=role.id)
        UserRoleCrud(db).create(user_role_in)

def initialize_db(db: Session) -> None:
    create_initial_super_admin_account(db)
    user = create_initial_super_admin_user(db)
    create_roles(db)
    set_super_admin_role_to_user(db, user)