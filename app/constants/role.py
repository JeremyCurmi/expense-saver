class Role:
    """
    Constants for user roles scoped in application
    """
    GUEST = {
        "name": "GUEST",
        "description": "A Guest Account"
    }

    ACCOUNT_USER = {
        "name": "ACCOUNT_ADMIN",
        "description": "Primary User of an account"
    }

    ACCOUNT_ADMIN = {
        "name": "ACCOUNT_ADMIN",
        "description": "Primary Administrator/Superuser For an Account"
    }

    ACCOUNT_MANAGER = {
        "name": "ACCOUNT_MANAGER",
        "description": "Day to Day Administrator of Events For an Account"
    }

    ADMIN = {
        "name": "ADMIN",
        "description": "Admin of Application"
    }

    SUPER_ADMIN = {
        "name": "SUPER_ADMIN",
        "description": "Super Administrator of Application"
    }

    all_users = [GUEST["name"],
                 ACCOUNT_USER["name"],
                 ACCOUNT_ADMIN["name"],
                 ACCOUNT_MANAGER["name"],
                 ADMIN["name"],
                 SUPER_ADMIN["name"],
                 ]

    registered_users = [ACCOUNT_USER["name"],
                 ACCOUNT_ADMIN["name"],
                 ACCOUNT_MANAGER["name"],
                 ADMIN["name"],
                 SUPER_ADMIN["name"],
                 ]

    admin_users = [ADMIN["name"],
                   SUPER_ADMIN["name"],
                   ]