import argparse
import os
from flask_cors import CORS
from app import create_app
from general_config import general_config

app = create_app(os.environ.get("FLASK_CONFIG", "default"))
app.secret_key = 'secret_key_1234345'
CORS(app)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host",
                        type=str,
                        default="0.0.0.0")
    parser.add_argument("--port",
                        type=int,
                        default=8001)
    args = parser.parse_args()
    app.run(host=args.host,
            port=args.port)
