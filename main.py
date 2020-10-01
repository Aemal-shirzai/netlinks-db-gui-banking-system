from connections import app, render_template
import admin
import users
import authentication
import password_reset

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run()