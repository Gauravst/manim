from manim import *

class FileFlowDiagram(Scene):
    def construct(self):
        # Text Style
        client_style = {"font_size": 24, "color": RED}
        server_style = {"font_size": 24, "color": ORANGE}
        discord_style = {"font_size": 24, "color": BLUE}
        box_style = {"stroke_color": GREEN, "stroke_width": 2, "fill_opacity": 0.1}

        # Titles
        client_text = Text("client", **client_style).to_edge(LEFT).shift(UP*2)
        server_text = Text("server", **server_style).shift(UP*2)
        discord_text = Text("discord", **discord_style).to_edge(RIGHT).shift(UP*2)

        # Client box
        client_box = Rectangle(width=1.8, height=0.8, **box_style).next_to(client_text, DOWN, buff=0.5)
        client_label = Text("file", **client_style).move_to(client_box)

        # Server boxes
        upload_box = Rectangle(width=2.8, height=0.8, **box_style).to_edge(UP).shift(DOWN)
        upload_label = Text("upload", **server_style).move_to(upload_box)

        link_db_box = Rectangle(width=3.8, height=1.2, **box_style).next_to(upload_box, DOWN, buff=1)
        link_db_label = Text("link\nsave in db", **server_style).move_to(link_db_box)

        # Discord box
        storage_box = Rectangle(width=2.8, height=0.8, **box_style).to_edge(RIGHT).shift(DOWN)
        storage_label = Text("storage", **discord_style).move_to(storage_box)

        # Download box (client)
        download_box = Rectangle(width=2.8, height=0.8, **box_style).next_to(client_box, DOWN, buff=2)
        download_label = Text("download\nbtn", **client_style).move_to(download_box)

        # Arrows
        arrow_client_to_server = Arrow(client_box.get_right(), upload_box.get_left(), buff=0.2)
        arrow_server_to_discord = Arrow(upload_box.get_right(), storage_box.get_left(), buff=0.2)
        arrow_discord_to_db = Arrow(storage_box.get_bottom(), link_db_box.get_top(), buff=0.2)
        arrow_db_to_download = Arrow(link_db_box.get_left(), download_box.get_right(), buff=0.2)

        # "Using bot" annotation
        bot_annotation = Text("using bot", font_size=18).next_to(arrow_server_to_discord, UP)

        # Animate Elements
        self.play(Write(client_text))
        self.play(FadeIn(client_box), Write(client_label))
        self.play(Write(server_text))
        self.play(FadeIn(upload_box), Write(upload_label))
        self.play(Write(discord_text))
        self.play(FadeIn(storage_box), Write(storage_label))
        self.play(FadeIn(link_db_box), Write(link_db_label))
        self.play(FadeIn(download_box), Write(download_label))

        # Animate Arrows
        self.play(GrowArrow(arrow_client_to_server))
        self.play(Write(bot_annotation))
        self.play(GrowArrow(arrow_server_to_discord))
        self.play(GrowArrow(arrow_discord_to_db))
        self.play(GrowArrow(arrow_db_to_download))

        # Hold the final frame
        self.wait(2)
