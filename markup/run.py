from markup.app.backend.api import Api
from markup.app.modules.toolbar import create_menu
from markup.common.temp import ReadConf
from markup.config import Config, webview

api = Api()
min_size = ReadConf.get_launcher_conf(Config.APP_PROFILE_DIR)
window = webview.create_window(
    "Untitled* - MarkUp",
    "app/frontend/main.html",
    width=min_size[0],
    height=min_size[1],
    min_size=(800, 600),
    js_api=api,
)
menu_items = create_menu(window)
webview.start(
    menu=menu_items,
    # debug=True,
    private_mode=True,
)
