from flask import Flask, request, abort
import time
app = Flask(__name__)
SECRET = "FLAG{SideChannel_Bypass}"
@app.route('/')
def index():
    return (
        "<h1>Vuln App</h1>"
        "<form method='get' action='/search'>"
        "<input name='q'><input type='submit'></form>"
    )
@app.route('/search')
def search():
    q = request.args.get('q', '')
    delay = 0.0
    for i, c in enumerate(SECRET):
        if i < len(q) and q[i] == c:
            delay += 0.5
        else:
            break
    time.sleep(delay)
    if "' OR '1'='1" in q:
        abort(403)

    return f"Search results for: {q}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)