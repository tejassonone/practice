import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        for i in range(5):
            self.response.write("Tejas,\n 33274,\n IT dept.\n")


app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug=True)
