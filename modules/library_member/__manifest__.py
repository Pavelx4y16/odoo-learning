{
    "name": "Library Members",
    "description": "Manage people who will be able to borrow books.",
    "author": "Pavel Savastseika",
    "depends": ["library_app"],
    "application": False,
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/member_view.xml"
    ]
}
