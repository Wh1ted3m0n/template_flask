from flask import Flask
import templetesART

# notate 1 воно динамічне можна не презапускати дотаток кожний раз
# main функція для запуску flask
app = Flask(__name__)
#декоратор який відстежує текущу сторінку
@app.route('/')
def home_print():
    return '''
<!doctype html>
<html lang="uk">
<head>
  <meta charset="utf-8" />
  <title>Random Image</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 2rem; }
    img { max-width: 100%; height: auto; border-radius: 12px; }
    button { padding: .6rem 1rem; border-radius: 10px; border: 1px solid #ddd; cursor: pointer; }
  </style>
</head>
<body>
  <button id="reload">Нова картинка</button>
  <div>
    <img id="pic" src="https://picsum.photos/800/500?random=1" alt="Random image">
  </div>

  <script>
    const img = document.getElementById('pic');
    document.getElementById('reload').addEventListener('click', () => {
      img.src = `https://picsum.photos/800/500?rand=${Math.random()}`;
    });
  </script>
</body>
</html>

    '''
@app.route('/about')
def about():
    return '''<!doctype html>
<html lang="uk">
<head>
  <meta charset="utf-8">
  <title>Dark Theme Page</title>
  <style>
    body {
      background-color: #000;  /* чорний фон */
      color: #fff;             /* білий текст */
      font-family: system-ui, sans-serif;
      margin: 2rem;
    }
    a {
      color: #4da6ff;          /* сині посилання */
    }
  </style>
</head>
<body>
  <h1>ITS WORKING</h1>
  
</body>
</html>
'''+templetesART.art1
@app.route('/page1')
def page1():
    return 'its working'
if __name__ == "__main__":
    app.run(debug=True)