# toolbar n main stuff
main_helper = """
ScreenManager:
    # self.root
    MainScreen:
        id: main
    VoiceScreen:
        id: voice
    ResultScreen:
        id: result

<MainScreen>:
    name: 'main'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Athena'
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        md_bg_color: [0, 0, 0 , 1]
                        specific_text_color: 1,1,1,1
                        elevation: 8
                    # main content of page goes here
                    Widget:
                MDTextField:
                    id: search
                    hint_text: '   Enter your search'
                    icon_right: 'magnify'
                    icon_right_color: 1,1,1,1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x: None
                    width: 300 
                MDRectangleFlatIconButton:
                    icon: 'magnify'
                    text: 'search'
                    pos_hint: {'center_x': 0.2, 'center_y': 0.42}
                    on_release: app.search() 
                    size_hint_x: None
                    width: 100
                # MDRoundFlatIconButton:
                #     icon: 'magnify'
                #     text: 'search'
                #     pos_hint: {'center_x': 0.4, 'center_y': 0.6}
                MDFloatingActionButton:
                    spacing: '3dp'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                    icon: 'microphone'
                    md_bg_color: [33 / 255, 33 / 255, 33 / 255, 1]
                    specific_text_color: 1,1,1,1
                    on_release: app.voice()
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                ScrollView:
                    MDFlatButton:
                        text: 'Help'       
<VoiceScreen>:
    name: 'voice'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Athena'
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        md_bg_color: [0, 0, 0 , 1]
                        specific_text_color: 1,1,1,1
                        elevation: 8
                    Widget:
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '10dp'
                    padding: '10dp'
                    MDLabel:
                        text: '     '
                        font_style: 'H4'
                        size_hint_y: None
                        height: self.texture_size[1]
                    ScrollView:
                        MDList:
                            id: messages     
                            MDRectangleFlatButton:
                                text: 'Begin'
                                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                                on_press: app.voices() 
                            MDLabel:
                                text: '    '
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]    
                MDFloatingActionButton:
                    spacing: '3dp'
                    pos_hint: {'center_x': 0.8, 'center_y': 0.1}
                    icon: 'arrow-left-thick'
                    md_bg_color: [33 / 255, 33 / 255, 33 / 255, 1]
                    specific_text_color: 1,1,1,1
                    on_release: root.manager.current = 'main'
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                ScrollView:
                    MDFlatButton:
                        text: 'Help'

<ResultScreen>:
    name: 'result'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Athena'
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        md_bg_color: [0, 0, 0 , 1]
                        specific_text_color: 1,1,1,1
                        elevation: 8
                    Widget:
                BoxLayout:
                    id: result_add
                    orientation: 'vertical'
                    padding: '10dp'
                    # main content goes here
                    MDLabel:
                        text: '    '
                        font_style: 'H2'
                        size_hint_y: None
                        height: self.texture_size[1]
                    ScrollView:
                        MDList:
                            id: text
                            Image:
                                source: 'test.jpg'
                                size_hint_y: None
                                width: 210
                                size_hint_x: None 
                                height: 210
                                allow_stretch: True
                                id: result_image
                            MDLabel:
                                text: '    '
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: 'Result'
                                font_style: 'Subtitle1'
                                size_hint_y: None
                                height: self.texture_size[1]
                            MDLabel:
                                text: '    '
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                MDFloatingActionButton:
                    spacing: '3dp'
                    pos_hint: {'center_x': 0.8, 'center_y': 0.1}
                    icon: 'home'
                    md_bg_color: [33 / 255, 33 / 255, 33 / 255, 1]
                    specific_text_color: 1,1,1,1
                    on_release: root.manager.current = 'main'
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                ScrollView:
                    MDFlatButton:
                        text: 'Help'
    
"""

# nm,
label_left = """
    MDLabel:
        text: ''
        font_style: 'Subtitle1'
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: 'Custom'
        halign: 'left'
        text_color: 1, 1, 1, 1
"""

label_right = """
    MDLabel:
        text: ''
        font_style: 'Subtitle1'
        size_hint_y: None
        height: self.texture_size[1]
        halign: 'right'
        theme_text_color: 'Custom'
        text_color: 1, 1, 1, 1
"""
