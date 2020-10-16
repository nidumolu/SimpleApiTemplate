import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from source.config import logger
ma = Marshmallow()


def init_api():
    logger.log_text('Initializing from Swagger.yaml', severity='INFO')
    app = connexion.App(__name__, specification_dir="./openapi/")
    app.add_api("swagger.yaml", arguments={"title": "files"})
    CORS(app.app)
    ma.init_app(app.app)
    return app
