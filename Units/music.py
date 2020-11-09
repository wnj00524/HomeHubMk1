import tekore as tk
import Units.tools as tools
def play_anti_flag():
    app_key = tools.get_setting("app_key","settings.npy")
    secret_key = tools.get_setting("secret_key","settings.npy")
    conf = (app_key, secret_key, "https://example.com/callback")
    token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
    #print(tools.get_setting("app_key"))
    spotify = tk.Spotify(token)
    tracks1 = spotify.album_tracks("3thDALJX9mvXyJVNSqHwd7")
    #tracks = spotify.current_user_top_tracks(limit=10)
    spotify.playback_start_tracks([t.id for t in tracks1.items])
