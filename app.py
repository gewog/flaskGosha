import datetime


from flask import Flask, render_template, request, redirect
from database_settings import settings, path_to_db
from datetime import datetime
from route_mho import main_bp


app = Flask(__name__)
app.register_blueprint(main_bp)
db = settings.get_db(app, path_to_db.path)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.intro}"



@app.route('/create',methods =['GET','POST'])
def create_article():
    """Функция создания статьи"""
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        res = Article(title=title, intro=intro, text=text)
        try:
            con = db.session
            con.add(res)
            con.commit()
            return redirect("/get_posts")
        except Exception as e:
            print(e)
    else:
        return render_template('create-article.html')

@app.route('/get_posts')
def get_posts():
    objects = Article.query.order_by(Article.date).all()[::-1]
    return render_template('all_articles.html', obj=objects)

@app.route('/post/<int:id>')
def read_full_post(id):
    result = Article.query.get(id)
    return render_template('full_post.html', result=result)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
