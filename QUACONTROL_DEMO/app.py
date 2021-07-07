from flask import Flask
import dash

server = Flask(__name__)

app_DONG_TIEN = dash.Dash(
        __name__,
        # server=server,
        url_base_pathname='/',
        # Tắt xác thực cuộc gọi Input, Output, State
        suppress_callback_exceptions=True
    )


