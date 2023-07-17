from odoo import http


class Book(http.Controller):
    @http.route("/library/books", auth="user")
    def list(self, **kwargs):
        book_model = http.request.env["library.book"]
        books = book_model.search([])

        return http.request.render("library_app.book_list_template", {"books": books})
