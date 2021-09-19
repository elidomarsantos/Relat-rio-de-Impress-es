from kivy.lang import Builder
from kivy.properties import ObjectProperty
import pandas as pd
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.effects import stiffscroll
import os
import sys



Window.size = (1200, 900)


KV = '''

<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Histórico de Impressões"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Impressões/Custos por Departamento"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

            OneLineListItem:
                text: "Impressões por Usuário"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
            
            OneLineListItem:
                text: "TOP 10 - Custos de Impressão por Departamento"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"

            OneLineListItem:
                text: "TOP 10 - Impressões por Departamento"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 5"   

            OneLineListItem:
                text: "TOP 10 - Impressões Coloridas"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 6"  

            OneLineListItem:
                text: "TOP 10 - Impressões por Usuário"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 7"                      
                        


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 20
        title: "Relatório de Impressoras"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        right_action_items: [['chart-arc', lambda x: app.gerar_report(), 'Atualizar Relatórios']]

    MDLabel:
        id: OK
        text:''
        halign: 'center'
        pos_hint: {"center_y": .1}
        theme_text_color: "Custom"
        text_color: 'B71C1C'
        font_size: 20


        


    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager




            MDScreen:
                name: "scr 1"

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "360dp"
                    pos_hint: {"center_x": .5, "center_y": .67}
                    padding: "8dp"


                    MDLabel:
                        text: "Total Iberostar no Mês"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDLabel:
                        text: "Hotel Bahia"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: h1_total
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: h1_custo
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                   
                    MDLabel:
                        text: "Hotel Praia do Forte"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color
                   
                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: h2_total
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        
                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: h2_custo
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'

                    MDLabel:
                        text: "Comuns"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: com_total
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: com_custo
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'

                    MDLabel:
                        text: "Complexo"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: total_geral
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: custo_geral
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'   
                            
                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "120dp"
                    pos_hint: {"center_x": .5, "center_y": .32}
                    padding: "8dp"


                    MDLabel:
                        text: "Média Mensal Iberostar"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "2019"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: mmedia_2019
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "2020"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: mmedia_2020
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'

                        MDLabel:
                            text: "2021"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: mmedia_2021
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'   

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "120dp"
                    pos_hint: {"center_x": .5, "center_y": .12}
                    padding: "8dp"


                    MDLabel:
                        text: "Total Geral Iberostar"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "2019"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: mtotal_2019
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "2020"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: mtotal_2020
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'

                        MDLabel:
                            text: "2021"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: mtotal_2021
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'                    

                
            MDScreen:
                name: "scr 2"


                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "120dp"
                    pos_hint: {"center_x": .65, "center_y": .77}
                    padding: "8dp"


                    MDLabel:
                        text: "Coloridas"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: cor_total
                            text: ''
                            halign: "center"
                        

                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: cor_custo
                            text: ''
                            halign: "center"
                
                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "120dp"
                    pos_hint: {"center_x": .65, "center_y": .57}
                    padding: "8dp"


                    MDLabel:
                        text: "P & B"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: pb_total
                            text: ''
                            halign: "center"
                        

                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: pb_custo
                            text: ''
                            halign: "center"  

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "120dp"
                    pos_hint: {"center_x": .65, "center_y": .37}
                    padding: "8dp"


                    MDLabel:
                        text: "Totais Departamento no Mês"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Unidades"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: total_dpto
                            text: ''
                            halign: "center"
                        

                        MDLabel:
                            text: "Custo"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: custo_dpto
                            text: ''
                            halign: "center"  

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "120dp"
                    pos_hint: {"center_x": .65, "center_y": .17}
                    padding: "8dp"


                    MDLabel:
                        text: "Média Mensal de Impressões do Departamento"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "2019"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: media_2019
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "2020"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: media_2020
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'

                        MDLabel:
                            text: "2021"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: media_2021
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'   
                
                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "420dp", "60dp"
                    pos_hint: {"center_x": .20, "center_y": .85}
                    padding: "8dp"


                    MDLabel:
                        text: "Selecione o departamento para visualizar"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color
            
                
                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "280dp", "710dp"
                    pos_hint: {"center_x": .20, "center_y": .42}

                    ScrollView:

                        MDList:
                            id: List_dpto

                            OneLineListItem:
                                text: "com_administracao"
                                on_release: app.com_adm()
                            OneLineListItem:
                                text: "com_almoxarifado"
                                on_release: app.com_alx()
                            OneLineListItem:
                                text: "com_animacao"   
                                on_release: app.com_anim() 
                            OneLineListItem:
                                text: "com_bares"
                                on_release: app.com_bar()
                            OneLineListItem:
                                text: "com_compras"    
                                on_release: app.com_comp()
                            OneLineListItem:
                                text: "com_cozinha"
                                on_release: app.com_coz()
                            OneLineListItem:
                                text: "com_direção"    
                                on_release: app.com_dir()
                            OneLineListItem:
                                text: "com_rrhh"    
                                on_release: app.com_rh()
                            OneLineListItem:
                                text: "com_golf"    
                                on_release: app.com_golf()
                            OneLineListItem:
                                text: "com_governança"
                                on_release: app.com_gov()
                            OneLineListItem:
                                text: "com_grupos"    
                                on_release: app.com_grup()
                            OneLineListItem:
                                text: "com_informatica"
                                on_release: app.com_info()
                            OneLineListItem:
                                text: "com_lavanderia"   
                                on_release: app.com_lav() 
                            OneLineListItem:
                                text: "com_manutencao"
                                on_release: app.com_man()
                            OneLineListItem:
                                text: "com_reservas"
                                on_release: app.com_res()
                            OneLineListItem:
                                text: "com_seguridad"
                                on_release: app.com_seg()
                            OneLineListItem:
                                text: "com_telefones"    
                                on_release: app.com_tel()
                            OneLineListItem:
                                text: "h1_animacao"    
                                on_release: app.h1_anim()
                            OneLineListItem:
                                text: "h1_bares"
                                on_release: app.h1_bar()
                            OneLineListItem:
                                text: "h1_cozinha"    
                                on_release: app.h1_coz()
                            OneLineListItem:
                                text: "h1_direcao"
                                on_release: app.h1_dir()
                            OneLineListItem:
                                text: "h1_governanta"    
                                on_release: app.h1_gov()
                            OneLineListItem:
                                text: "h1_manutencao"
                                on_release: app.h1_man()
                            OneLineListItem:
                                text: "h1_recepcao"    
                                on_release: app.h1_recep()
                            OneLineListItem:
                                text: "h1_rrpp"
                                on_release: app.h1_rp()
                            OneLineListItem:
                                text: "h2_animacao"
                                on_release: app.h2_anim()
                            OneLineListItem:
                                text: "h2_bares"    
                                on_release: app.h2_bar()
                            OneLineListItem:
                                text: "h2_cozinha"
                                on_release: app.h2_coz()
                            OneLineListItem:
                                text: "h2_direcao"    
                                on_release: app.h2_dir()
                            OneLineListItem:
                                text: "h2_governanta"
                                on_release: app.h2_gov()
                            OneLineListItem:
                                text: "h2_manutencao"
                                on_release: app.h2_man()
                            OneLineListItem:
                                text: "h2_recepcao"
                                on_release: app.h2_recep()
                            OneLineListItem:
                                text: "h2_rrpp"          
                                on_release: app.h2_rp()  
                            OneLineListItem:
                                text: "Escritório_Salvador"          
                                on_release: app.salvador()      

            MDScreen:
                name: "scr 3"

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "280dp", "710dp"
                    pos_hint: {"center_x": .15, "center_y": .455}

                    ScrollView:

                        MDList:
                            id: usuarios
                          

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "560dp", "180dp"
                    pos_hint: {"center_x": .65, "center_y": .50}
                    padding: "8dp"


                    MDLabel:
                        text: "Total de Impressões"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_dark

                    MDCard:
                        orientation: 'horizontal'
                        elevation:20
                        

                        MDLabel:
                            text: "Há 02 meses"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light 

                        MDLabel:
                            id: ante_anterior
                            text: ''
                            halign: "center"
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'
                        

                        MDLabel:
                            text: "Mês Anterior"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: anterior
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C'

                        MDLabel:
                            text: "Mês Atual"
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light       
                    
                        MDLabel:
                            id: atual
                            text: ''
                            halign: "center"  
                            bold: 'True'
                            theme_text_color: "Custom"
                            text_color: 'B71C1C' 

                MDRaisedButton:
                    text: "Gerar Relatório"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .5, "center_y": .10} 
                    bold: 'True'
                    font_size: "18sp"   
                    on_release: app.consulta_users() 


            MDScreen:
                name: "scr 4"

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "740dp", "60dp"
                    pos_hint: {"center_x": .5, "center_y": .85}
                    padding: "8dp"


                    MDLabel:
                        text: "TOP 10 - Custos de Impressão por Departamento"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color
                    

                MDCard:
                    orientation: 'horizontal'
                    elevation:20
                    size_hint: None, None
                    size: "580dp", "560dp"
                    pos_hint: {"center_x": .5, "center_y": .425}
                    padding: "8dp"
                    halign: "center"

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Departamento'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light      

                        MDList:
                            id: top10_impress
                            
                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Custo'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light          
            

                        MDList:
                            id: top10_impress1

                MDRaisedButton:
                    text: "Gerar Relatório"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .5, "center_y": .10} 
                    bold: 'True'
                    font_size: "18sp"   
                    on_release: app.top10_custos()    
                            
                   
            MDScreen:
                name: "scr 5"

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "920dp", "80dp"
                    pos_hint: {"center_x": .5, "center_y": .85}
                    padding: "8dp"


                    MDLabel:
                        text: "TOP 10 - Impressões por Departamento"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color

                    

                MDCard:
                    orientation: 'horizontal'
                    elevation:20
                    size_hint: None, None
                    size: "920dp", "540dp"
                    pos_hint: {"center_x": .5, "center_y": .425}
                    padding: "8dp"
                    halign: "center"

                    
                    MDCard:
                        elevation:20
                        orientation: 'vertical'


                        MDLabel:
                            text: 'Departamento'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light   

                        MDList:
                            id: top10_media

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Total Mês' 
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light         
    
                        MDList:
                            id: top10_media1
                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Média Mensal 2019' 
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light          

                    
                        MDList:
                            id: top10_media2

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Média Mensal 2020'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light   

                        MDList:
                            id: top10_media3

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Média Mensal 2021'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light                   

                        MDList:
                            id: top10_media4
                MDRaisedButton:
                    text: "Gerar Relatório"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .5, "center_y": .10} 
                    bold: 'True'
                    font_size: "18sp"   
                    on_release: app.top10_imp()   
            
            MDScreen:
                name: "scr 6" 

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "740dp", "60dp"
                    pos_hint: {"center_x": .5, "center_y": .85}
                    padding: "8dp"


                    MDLabel:
                        text: "TOP 10 - Impressões Coloridas"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color
                    

                MDCard:
                    orientation: 'horizontal'
                    elevation:20
                    size_hint: None, None
                    size: "580dp", "560dp"
                    pos_hint: {"center_x": .5, "center_y": .425}
                    padding: "8dp"
                    halign: "center"

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Departamento'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light                   


                        MDList:
                            id: top10_cor

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Páginas Coloridas'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light            
                        
                        MDList:
                            id: top10_cor1              
                
                MDRaisedButton:
                    text: "Gerar Relatório"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .5, "center_y": .10} 
                    bold: 'True'
                    font_size: "18sp"   
                    on_release: app.top10_cor()  

            MDScreen:
                name: "scr 7"

                MDCard:
                    orientation: 'vertical'
                    elevation:20
                    size_hint: None, None
                    size: "920dp", "80dp"
                    pos_hint: {"center_x": .5, "center_y": .85}
                    padding: "8dp"


                    MDLabel:
                        text: "TOP 10 - Impressões por Usuário"
                        theme_text_color: 'Custom'
                        text_color: 'F8F8FF'
                        bold: 'True'
                        halign: "center"
                        md_bg_color: app.theme_cls.primary_color

                    

                MDCard:
                    orientation: 'horizontal'
                    elevation:20
                    size_hint: None, None
                    size: "920dp", "540dp"
                    pos_hint: {"center_x": .5, "center_y": .425}
                    padding: "8dp"
                    halign: "center"

                    
                    MDCard:
                        elevation:20
                        orientation: 'vertical'


                        MDLabel:
                            text: 'Usuário'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light   

                        
                        MDList:
                            id: top20_user

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Mês Atual' 
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light         
    
                       

                        MDList:
                            id: top20_user1
                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Mês Anterior' 
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light          

                                    

                        MDList:
                            id: top20_user2

                    MDCard:
                        elevation:20
                        orientation: 'vertical'

                        MDLabel:
                            text: 'Há Dois Meses'
                            theme_text_color: 'Custom'
                            text_color: '000000'
                            bold: 'True'
                            halign: "center"
                            md_bg_color: app.theme_cls.primary_light   

                      

                        MDList:
                            id: top20_user3

                MDRaisedButton:
                    text: "Gerar Relatório"
                    md_bg_color: app.theme_cls.primary_color
                    pos_hint: {"center_x": .5, "center_y": .10} 
                    bold: 'True'
                    font_size: "18sp"   
                    on_release: app.top10_user()    



        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

            
    
'''

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class Report_Printer(MDApp):
    
    def gerar_report(self):
        global df
        global usuario_atual
        global usuario_anterior
        global usuario_dois_meses

        df = pd.read_excel('log_geral_atual.xlsx', skiprows=[0, 1])
        atual = pd.read_excel('log_geral_atual.xlsx', skiprows=[0, 1])
        usuario_atual = atual.groupby(['Nome completo']).sum()
        usuario_atual.to_excel('usuario_atual.xlsx')
        anterior = pd.read_excel('log_geral_anterior.xlsx', skiprows=[0, 1])
        usuario_anterior = anterior.groupby(['Nome completo']).sum()
        usuario_anterior.to_excel('usuario_anterior.xlsx')
        dois_meses = pd.read_excel('log_geral_2_meses.xlsx', skiprows=[0, 1])
        usuario_dois_meses = dois_meses.groupby(['Nome completo']).sum()
        usuario_dois_meses.to_excel('usuario_dois_meses.xlsx')
        
        usuario_anterior.reset_index(level=0, inplace=True)
        usuario_dois_meses.reset_index(level=0, inplace=True)
        df.drop(columns=['Conta cobrada', 'Nome da conta compartilhada', 'Código da conta compartilhada',
                         'Nome da conta compartilhada pai', 'Código da conta compartilhada pai',
                         'Sub-nome da conta compartilhada', 'Sub-código da conta compartilhada',
                         'Servidor de impressão', 'Identificador de impressora física', 'Tipo/Modelo da Impressora',
                         'Tipo de Uso', 'Páginas coloridas estimadas', 'Cópias', 'Custo', 'Tamanho do Papel',
                         'Largura do papel (mm)', 'Largura do papel (mm)', 'Altura do papel (mm)', 'Duplo',
                         'Escala de Cinza', 'Faturado', 'Cliente', 'Tamanho (KB)', 'Linguagem da Impressora',
                         'Comentário', 'Impresso', 'Cancelado', 'Reembolsado', 'Permitido', 'Razão do Bloqueio',
                         'Arquivado', 'Offline'], inplace=True)
        df['Total de páginas P&B'] = 0
        df.loc[df['Total de páginas coloridas'] == 0, 'Total de páginas P&B'] = df['Total Páginas impressas']
        df['Número de série da impressora'].fillna('ND', inplace=True)
        df.to_excel('log_geral_tratado_atual.xlsx')

   

    def on_start(self):

        global usuario_atual
        global usuario_anterior
        global usuario_dois_meses
 
        df_imp = pd.read_excel('grupo_sumario_imp.xlsx', skiprows=[0, 1])
        df_imp.drop(df_imp.loc[df_imp['Grupo'] == '[Todos Usuários]'].index, inplace=True)
        df_imp.drop(columns=['Paginas Duplex', 'Paginas Simplex', 'Total Trab.', 'Média de Páginas', 'Custo Total',
                         'Custo Médio'], inplace=True)
        df_imp['Número de série da impressora'].fillna('ND', inplace=True)
        df_impress = df_imp.groupby(['Nome da Impressora', 'Número de série da impressora']).sum()
        df_impress.to_excel('report_por_impressora(enviar_JRB).xlsx')

        df_dpto = pd.read_excel('grupo_sumario_imp.xlsx', skiprows=[0, 1])
        df_dpto.drop(df_dpto.loc[df_dpto['Grupo'] == '[Todos Usuários]'].index, inplace=True)
        df_dpto.drop(columns=['Paginas Duplex', 'Paginas Simplex', 'Total Trab.', 'Média de Páginas', 'Custo Total',
                         'Custo Médio'], inplace=True)
        df_dptomento = df_dpto.groupby(['Grupo']).sum()
        df_dptomento['Custo Coloridas'] = (df_dptomento['Páginas coloridas'] * 0.47618584).round(2)
        df_dptomento['Custo P & B'] = (df_dptomento['Páginas Escala de Cinza'] * 0.0476186).round(2)
        df_dptomento['Custo Departamento'] = (df_dptomento['Custo Coloridas'] + df_dptomento['Custo P & B']).round(2)
        df_dptomento.to_excel('report_por_dpto1.xlsx')
        df_dptomento1 =pd.read_excel('report_por_dpto1.xlsx')
        df_dptomento1 = df_dptomento1.append({'Grupo':'com_Escritório_Salvador', 'Páginas coloridas': 0, 'Páginas Escala de Cinza': 0, 'Total Páginas impressas': 0, 'Custo Coloridas': 0, 'Custo P & B': 0, 'Custo Departamento': 0}, ignore_index=True) 
        df_dptomento1.to_excel('report_por_dpto.xlsx')
        total_dpto = df_dptomento1['Total Páginas impressas'].sum()
        self.root.ids.total_geral.text = (f'{total_dpto}')
        total_custo = df_dptomento1['Custo Departamento'].sum()
        self.root.ids.custo_geral.text = (f'R$ {total_custo:.2f}')
        total_com = df_dptomento1[df_dptomento1['Grupo'].str.contains('com_')]
        soma_total_com = total_com['Total Páginas impressas'].sum()
        self.root.ids.com_total.text = (f'{soma_total_com}')
        total_h1 = df_dptomento1[df_dptomento1['Grupo'].str.contains('h1_')]
        soma_total_h1 = total_h1['Total Páginas impressas'].sum()
        self.root.ids.h1_total.text = (f'{soma_total_h1}')
        total_h2 = df_dptomento1[df_dptomento1['Grupo'].str.contains('h2_')]
        soma_total_h2 = total_h2['Total Páginas impressas'].sum()
        self.root.ids.h2_total.text = (f'{soma_total_h2}')
        custo_com = df_dptomento1[df_dptomento1['Grupo'].str.contains('com_')]
        custo_total_com = custo_com['Custo Departamento'].sum()
        self.root.ids.com_custo.text = (f'R$ {custo_total_com:.2f}')
        custo_h1 = df_dptomento1[df_dptomento1['Grupo'].str.contains('h1_')]
        custo_total_h1 = custo_h1['Custo Departamento'].sum()
        self.root.ids.h1_custo.text = (f'R$ {custo_total_h1:.2f}')
        custo_h2 = df_dptomento1[df_dptomento1['Grupo'].str.contains('h2_')]
        custo_total_h2 = custo_h2['Custo Departamento'].sum()
        self.root.ids.h2_custo.text = (f'R$ {custo_total_h2:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mgeral = medias.loc[medias['Departamento'] == 'geral', 2019].values[0]
        self.root.ids.mmedia_2019.text = (f'{mgeral:.0f}')
        mgeral1 = medias.loc[medias['Departamento'] == 'geral', 2020].values[0]
        self.root.ids.mmedia_2020.text = (f'{mgeral1:.0f}')
        mgeral2 = medias.loc[medias['Departamento'] == 'geral', 2021].values[0]
        self.root.ids.mmedia_2021.text = (f'{mgeral2:.0f}')
        mtotal = medias.loc[medias['Departamento'] == 'geral', 'total_2019'].values[0]
        self.root.ids.mtotal_2019.text = (f'{mtotal:.0f}')
        mtotal1 = medias.loc[medias['Departamento'] == 'geral', 'total_2020'].values[0]
        self.root.ids.mtotal_2020.text = (f'{mtotal1:.0f}')
        mtotal2 = medias.loc[medias['Departamento'] == 'geral', 'total_2021'].values[0]
        self.root.ids.mtotal_2021.text = (f'{mtotal2:.0f}')
        
        #BUSCAR IMPRESSÕES POR USUÁRIO PERÍODO ATUAL
    def consulta_users(self):    
        usuario_atual = pd.read_excel('usuario_atual.xlsx')
        usuario_atual.reset_index(level=0, inplace=True)
        lista_nomes = usuario_atual['Nome completo'].tolist()
        for usuarios in lista_nomes:
            self.root.ids.usuarios.add_widget(OneLineListItem(text=f'{usuarios}', on_press= self.nomear))
        
       
        #FILTRAR TOP 10 CUSTOS DE IMPRESSÃO
    def top10_custos(self):       
        df =  pd.read_excel('report_por_dpto.xlsx')
        df1= df.sort_values(by=["Custo Departamento"], ascending=False).head(10)
        df1.reset_index(drop=True)
        grupos = df1['Grupo'].to_list()
        for grupo in grupos:
            self.root.ids.top10_impress.add_widget(OneLineListItem(text=f'                  {grupo}'))
        custos = df1['Custo Departamento'].to_list()   
        for custo in custos:
            self.root.ids.top10_impress1.add_widget(OneLineListItem(text=f'                        R$ {custo}'))
      
        #FILTRAR TOP 10 IMPRESSÕES POR DPTO
    def top10_imp(self):       
        df2 =  pd.read_excel('medias.xlsx', skipfooter=1)
        df3= df2.sort_values(by=["mês_atual"], ascending=False).head(10)
        df3.reset_index(drop=True)
        hist_dptos = df3['Departamento'].tolist()
        for hist_dpto in hist_dptos:
            self.root.ids.top10_media.add_widget(OneLineListItem(text=f'{hist_dpto}'))
        hist_dptos1 = df3['mês_atual'].tolist()
        for hist_dpto1 in hist_dptos1:
            self.root.ids.top10_media1.add_widget(OneLineListItem(text=f'             {hist_dpto1:.0f}'))
        hist_dptos2 = df3[2019].tolist()
        for hist_dpto2 in hist_dptos2:
            self.root.ids.top10_media2.add_widget(OneLineListItem(text=f'             {hist_dpto2:.0f}')) 
        hist_dptos3 = df3[2020].tolist()
        for hist_dpto3 in hist_dptos3:
            self.root.ids.top10_media3.add_widget(OneLineListItem(text=f'             {hist_dpto3:.0f}'))  
        hist_dptos4 = df3[2021].tolist()
        for hist_dpto4 in hist_dptos4:
            self.root.ids.top10_media4.add_widget(OneLineListItem(text=f'             {hist_dpto4:.0f}'))     

        #FILTRAR TOP 10 IMPRESSÕES COLORIDAS
    def top10_cor(self):       
        df9 =  pd.read_excel('report_por_dpto.xlsx')
        df10= df9.sort_values(by=["Páginas coloridas"], ascending=False).head(10)
        df10.reset_index(drop=True)
        cores = df10['Grupo'].to_list()
        for cor in cores:
            self.root.ids.top10_cor.add_widget(OneLineListItem(text=f'                  {cor}'))
        cores1 = df10['Páginas coloridas'].tolist()
        for cor1 in cores1:
            self.root.ids.top10_cor1.add_widget(OneLineListItem(text=f'                            {cor1:.0f}'))   

        #FILTRAR TOP 10 USUÁRIOS
    def top10_user(self):       
        atual = pd.read_excel('usuario_atual.xlsx')
        anterior = pd.read_excel('usuario_anterior.xlsx')
        dois_meses = pd.read_excel('usuario_dois_meses.xlsx')
        usu_unit = atual.merge(anterior,on='Nome completo').merge(dois_meses,on='Nome completo')
        usu_unit.to_excel('usuarios_3_meses.xlsx')    
        usu_unit_filtro= usu_unit.sort_values(by=["Total Páginas impressas_x"], ascending=False).head(10)
        nomes = usu_unit_filtro['Nome completo'].to_list()
        page_atual = usu_unit_filtro['Total Páginas impressas_x'].to_list()
        page_anterior = usu_unit_filtro['Total Páginas impressas_y'].to_list()
        page_2meses = usu_unit_filtro['Total Páginas impressas'].to_list()
        for p1 in nomes:
            self.root.ids.top20_user.add_widget(OneLineListItem(text=f'{p1}'))
        for p2 in page_atual:
            self.root.ids.top20_user1.add_widget(OneLineListItem(text=f'               {p2:.0f}'))   
        for p3 in page_anterior:
            self.root.ids.top20_user2.add_widget(OneLineListItem(text=f'               {p3:.0f}')) 
        for p4 in page_2meses:
            self.root.ids.top20_user3.add_widget(OneLineListItem(text=f'               {p4:.0f}'))                
   

    def nomear(self, onelinelistitem):
        usuario_atual = pd.read_excel('usuario_atual.xlsx')
        atual = usuario_atual.loc[usuario_atual['Nome completo'] == onelinelistitem.text, 'Total Páginas impressas'].values[0]
        self.root.ids.atual.text = (f'{atual:.0f}')
        try:
            usuario_anterior = pd.read_excel('usuario_anterior.xlsx')
            anterior = usuario_anterior.loc[usuario_anterior['Nome completo'] == onelinelistitem.text, 'Total Páginas impressas'].values[0]
            self.root.ids.anterior.text = (f'{anterior:.0f}')  
        except:
            self.root.ids.anterior.text = ('Sem Impressões')  
        try:     
            usuario_dois_meses = pd.read_excel('usuario_dois_meses.xlsx')
            dois_meses = usuario_dois_meses.loc[usuario_dois_meses['Nome completo'] == onelinelistitem.text, 'Total Páginas impressas'].values[0]
            self.root.ids.ante_anterior.text = (f'{dois_meses:.0f}')   
        except:
            self.root.ids.ante_anterior.text = ('Sem Impressões')  


    
    def com_adm(self):
        com_adm = pd.read_excel('report_por_dpto.xlsx')
        adm = com_adm.loc[com_adm['Grupo'] == 'com_administracao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{adm:.0f}')
        adm1 = com_adm.loc[com_adm['Grupo'] == 'com_administracao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {adm1:.2f}')
        adm2 = com_adm.loc[com_adm['Grupo'] == 'com_administracao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{adm2:.0f}')
        adm3 = com_adm.loc[com_adm['Grupo'] == 'com_administracao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {adm3:.2f}')
        adm4 = com_adm.loc[com_adm['Grupo'] == 'com_administracao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{adm4:.0f}')
        adm5 = com_adm.loc[com_adm['Grupo'] == 'com_administracao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {adm5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        madm = medias.loc[medias['Departamento'] == 'com_administracao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{madm:.0f}')
        madm1 = medias.loc[medias['Departamento'] == 'com_administracao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{madm1:.0f}')
        madm2 = medias.loc[medias['Departamento'] == 'com_administracao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{madm2:.0f}')
        




    def com_alx(self):
        almox = pd.read_excel('report_por_dpto.xlsx')
        com_alx = almox.loc[almox['Grupo'] == 'com_almoxarifado', 'Páginas coloridas'].values[0]
        h1_alx = almox.loc[almox['Grupo'] == 'h1_almoxarifado', 'Páginas coloridas'].values[0]
        h2_alx = almox.loc[almox['Grupo'] == 'h2_almoxarifado', 'Páginas coloridas'].values[0] 
        soma_cor_alx = com_alx + h1_alx + h2_alx
        self.root.ids.cor_total.text = (f'{soma_cor_alx}')
        com_alx1 = almox.loc[almox['Grupo'] == 'com_almoxarifado', 'Custo Coloridas'].values[0]
        h1_alx1 = almox.loc[almox['Grupo'] == 'h1_almoxarifado', 'Custo Coloridas'].values[0]
        h2_alx1 = almox.loc[almox['Grupo'] == 'h2_almoxarifado', 'Custo Coloridas'].values[0] 
        soma_cor_alx1 = com_alx1 + h1_alx1 + h2_alx1
        self.root.ids.cor_custo.text = (f'{soma_cor_alx1:.2f}')
        com_alx2 = almox.loc[almox['Grupo'] == 'com_almoxarifado', 'Páginas Escala de Cinza'].values[0]
        h1_alx2 = almox.loc[almox['Grupo'] == 'h1_almoxarifado', 'Páginas Escala de Cinza'].values[0]
        h2_alx2 = almox.loc[almox['Grupo'] == 'h2_almoxarifado', 'Páginas Escala de Cinza'].values[0] 
        soma_cor_alx2 = com_alx2 + h1_alx2 + h2_alx2
        self.root.ids.pb_total.text = (f'{soma_cor_alx2}')
        com_alx3 = almox.loc[almox['Grupo'] == 'com_almoxarifado', 'Custo P & B'].values[0]
        h1_alx3 = almox.loc[almox['Grupo'] == 'h1_almoxarifado', 'Custo P & B'].values[0]
        h2_alx3 = almox.loc[almox['Grupo'] == 'h2_almoxarifado', 'Custo P & B'].values[0] 
        soma_cor_alx3 = com_alx3 + h1_alx3 + h2_alx3
        self.root.ids.pb_custo.text = (f'{soma_cor_alx3:.2f}')
        com_alx4 = almox.loc[almox['Grupo'] == 'com_almoxarifado', 'Total Páginas impressas'].values[0]
        h1_alx4 = almox.loc[almox['Grupo'] == 'h1_almoxarifado', 'Total Páginas impressas'].values[0]
        h2_alx4 = almox.loc[almox['Grupo'] == 'h2_almoxarifado', 'Total Páginas impressas'].values[0] 
        soma_cor_alx4 = com_alx4 + h1_alx4 + h2_alx4
        self.root.ids.total_dpto.text = (f'{soma_cor_alx4}')
        com_alx5 = almox.loc[almox['Grupo'] == 'com_almoxarifado', 'Custo Departamento'].values[0]
        h1_alx5 = almox.loc[almox['Grupo'] == 'h1_almoxarifado', 'Custo Departamento'].values[0]
        h2_alx5 = almox.loc[almox['Grupo'] == 'h2_almoxarifado', 'Custo Departamento'].values[0] 
        soma_cor_alx5 = com_alx5 + h1_alx5 + h2_alx5
        self.root.ids.custo_dpto.text = (f'{soma_cor_alx5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        malx = medias.loc[medias['Departamento'] == 'com_almoxarifado', 2019].values[0]
        self.root.ids.media_2019.text = (f'{malx:.0f}')
        malx1= medias.loc[medias['Departamento'] == 'com_almoxarifado', 2020].values[0]
        self.root.ids.media_2020.text = (f'{malx1:.0f}')
        malx2= medias.loc[medias['Departamento'] == 'com_almoxarifado', 2021].values[0]
        self.root.ids.media_2021.text = (f'{malx2:.0f}')


    def com_anim(self):
        com_anim = pd.read_excel('report_por_dpto.xlsx')
        anim = com_anim.loc[com_anim['Grupo'] == 'com_animacao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{anim}')
        anim1 = com_anim.loc[com_anim['Grupo'] == 'com_animacao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {anim1:.2f}')
        anim2 = com_anim.loc[com_anim['Grupo'] == 'com_animacao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{anim2}')
        anim3 = com_anim.loc[com_anim['Grupo'] == 'com_animacao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {anim3:.2f}')
        anim4 = com_anim.loc[com_anim['Grupo'] == 'com_animacao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{anim4}')
        anim5 = com_anim.loc[com_anim['Grupo'] == 'com_animacao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {anim5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        manim = medias.loc[medias['Departamento'] == 'com_animacao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{manim:.0f}')
        manim1= medias.loc[medias['Departamento'] == 'com_animacao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{manim1:.0f}')
        manim2= medias.loc[medias['Departamento'] == 'com_animacao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{manim2:.0f}')
    
    def com_bar(self):
        com_bar = pd.read_excel('report_por_dpto.xlsx')
        bar = com_bar.loc[com_bar['Grupo'] == 'com_bares', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{bar}')
        bar1 = com_bar.loc[com_bar['Grupo'] == 'com_bares', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {bar1:.2f}')
        bar2 = com_bar.loc[com_bar['Grupo'] == 'com_bares', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{bar2}')
        bar3 = com_bar.loc[com_bar['Grupo'] == 'com_bares', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {bar3:.2f}')
        bar4 = com_bar.loc[com_bar['Grupo'] == 'com_bares', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{bar4}')
        bar5 = com_bar.loc[com_bar['Grupo'] == 'com_bares', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {bar5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mbar = medias.loc[medias['Departamento'] == 'com_bares', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mbar:.0f}')
        mbar1= medias.loc[medias['Departamento'] == 'com_bares', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mbar1:.0f}')
        mbar2= medias.loc[medias['Departamento'] == 'com_bares', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mbar2:.0f}')
        
        
    def com_comp(self):
        com_comp = pd.read_excel('report_por_dpto.xlsx')
        comp = com_comp.loc[com_comp['Grupo'] == 'com_compras', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{comp}')
        comp1 = com_comp.loc[com_comp['Grupo'] == 'com_compras', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {comp1:.2f}')
        comp2 = com_comp.loc[com_comp['Grupo'] == 'com_compras', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{comp2}')
        comp3 = com_comp.loc[com_comp['Grupo'] == 'com_compras', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {comp3:.2f}')
        comp4 = com_comp.loc[com_comp['Grupo'] == 'com_compras', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{comp4}')
        comp5 = com_comp.loc[com_comp['Grupo'] == 'com_compras', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {comp5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mcomp = medias.loc[medias['Departamento'] == 'com_compras', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mcomp:.0f}')
        mcomp1= medias.loc[medias['Departamento'] == 'com_compras', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mcomp1:.0f}')
        mcomp2= medias.loc[medias['Departamento'] == 'com_compras', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mcomp2:.0f}')

    def com_coz(self):
        com_coz = pd.read_excel('report_por_dpto.xlsx')
        coz = com_coz.loc[com_coz['Grupo'] == 'com_cozinha', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{coz}')
        coz1 = com_coz.loc[com_coz['Grupo'] == 'com_cozinha', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {coz1:.2f}')
        coz2 = com_coz.loc[com_coz['Grupo'] == 'com_cozinha', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{coz2}')
        coz3 = com_coz.loc[com_coz['Grupo'] == 'com_cozinha', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {coz3:.2f}')
        coz4 = com_coz.loc[com_coz['Grupo'] == 'com_cozinha', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{coz4}')
        coz5 = com_coz.loc[com_coz['Grupo'] == 'com_cozinha', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {coz5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mcoz = medias.loc[medias['Departamento'] == 'com_cozinha', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mcoz:.0f}')
        mcoz1= medias.loc[medias['Departamento'] == 'com_cozinha', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mcoz1:.0f}')
        mcoz2= medias.loc[medias['Departamento'] == 'com_cozinha', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mcoz2:.0f}')
        
    def com_dir(self):
        com_dir = pd.read_excel('report_por_dpto.xlsx')
        dir = com_dir.loc[com_dir['Grupo'] == 'com_direção', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{dir}')
        dir1 = com_dir.loc[com_dir['Grupo'] == 'com_direção', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {dir1:.2f}')
        dir2 = com_dir.loc[com_dir['Grupo'] == 'com_direção', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{dir2}')
        dir3 = com_dir.loc[com_dir['Grupo'] == 'com_direção', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {dir3:.2f}')
        dir4 = com_dir.loc[com_dir['Grupo'] == 'com_direção', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{dir4}')
        dir5 = com_dir.loc[com_dir['Grupo'] == 'com_direção', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {dir5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mdir = medias.loc[medias['Departamento'] == 'com_direção', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mdir:.0f}')
        mdir1= medias.loc[medias['Departamento'] == 'com_direção', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mdir1:.0f}')
        mdir2= medias.loc[medias['Departamento'] == 'com_direção', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mdir2:.0f}')
            
    def com_golf(self):
        com_golf = pd.read_excel('report_por_dpto.xlsx')
        golf = com_golf.loc[com_golf['Grupo'] == 'com_golf', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{golf}')
        golf1 = com_golf.loc[com_golf['Grupo'] == 'com_golf', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {golf1:.2f}')
        golf2 = com_golf.loc[com_golf['Grupo'] == 'com_golf', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{golf2}')
        golf3 = com_golf.loc[com_golf['Grupo'] == 'com_golf', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {golf3:.2f}')
        golf4 = com_golf.loc[com_golf['Grupo'] == 'com_golf', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{golf4}')
        golf5 = com_golf.loc[com_golf['Grupo'] == 'com_golf', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {golf5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mgolf = medias.loc[medias['Departamento'] == 'com_golf', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mgolf:.0f}')
        mgolf1= medias.loc[medias['Departamento'] == 'com_golf', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mgolf1:.0f}')
        mgolf2= medias.loc[medias['Departamento'] == 'com_golf', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mgolf2:.0f}')
            
        
    def com_gov(self):
        com_gov = pd.read_excel('report_por_dpto.xlsx')
        gov = com_gov.loc[com_gov['Grupo'] == 'com_governança', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{gov}')
        gov1 = com_gov.loc[com_gov['Grupo'] == 'com_governança', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {gov1:.2f}')
        gov2 = com_gov.loc[com_gov['Grupo'] == 'com_governança', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{gov2}')
        gov3 = com_gov.loc[com_gov['Grupo'] == 'com_governança', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {gov3:.2f}')
        gov4 = com_gov.loc[com_gov['Grupo'] == 'com_governança', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{gov4}')
        gov5 = com_gov.loc[com_gov['Grupo'] == 'com_governança', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {gov5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mgov = medias.loc[medias['Departamento'] == 'com_governança', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mgov:.0f}')
        mgov1= medias.loc[medias['Departamento'] == 'com_governança', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mgov1:.0f}')
        mgov2= medias.loc[medias['Departamento'] == 'com_governança', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mgov2:.0f}')

    def com_grup(self):
        com_grup = pd.read_excel('report_por_dpto.xlsx')
        grup = com_grup.loc[com_grup['Grupo'] == 'com_grupos', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{grup}')
        grup1 = com_grup.loc[com_grup['Grupo'] == 'com_grupos', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {grup1:.2f}')
        grup2 = com_grup.loc[com_grup['Grupo'] == 'com_grupos', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{grup2}')
        grup3 = com_grup.loc[com_grup['Grupo'] == 'com_grupos', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {grup3:.2f}')
        grup4 = com_grup.loc[com_grup['Grupo'] == 'com_grupos', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{grup4}')
        grup5 = com_grup.loc[com_grup['Grupo'] == 'com_grupos', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {grup5:.2f}') 
        medias = pd.read_excel('medias.xlsx')
        mgrup = medias.loc[medias['Departamento'] == 'com_grupos', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mgrup:.0f}')
        mgrup1= medias.loc[medias['Departamento'] == 'com_grupos', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mgrup1:.0f}')
        mgrup2= medias.loc[medias['Departamento'] == 'com_grupos', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mgrup2:.0f}')    
    
    def com_info(self):
        com_info = pd.read_excel('report_por_dpto.xlsx')
        info = com_info.loc[com_info['Grupo'] == 'com_informatica', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{info}')
        info1 = com_info.loc[com_info['Grupo'] == 'com_informatica', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {info1:.2f}')
        info2 = com_info.loc[com_info['Grupo'] == 'com_informatica', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{info2}')
        info3 = com_info.loc[com_info['Grupo'] == 'com_informatica', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {info3:.2f}')
        info4 = com_info.loc[com_info['Grupo'] == 'com_informatica', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{info4}')
        info5 = com_info.loc[com_info['Grupo'] == 'com_informatica', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {info5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        minfo = medias.loc[medias['Departamento'] == 'com_informatica', 2019].values[0]
        self.root.ids.media_2019.text = (f'{minfo:.0f}')
        minfo1= medias.loc[medias['Departamento'] == 'com_informatica', 2020].values[0]
        self.root.ids.media_2020.text = (f'{minfo1:.0f}')  
        minfo2= medias.loc[medias['Departamento'] == 'com_informatica', 2021].values[0]
        self.root.ids.media_2021.text = (f'{minfo2:.0f}')  
    
    
        
    def com_lav(self):
        com_lav = pd.read_excel('report_por_dpto.xlsx')
        lav = com_lav.loc[com_lav['Grupo'] == 'com_lavanderia', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{lav}')
        lav1 = com_lav.loc[com_lav['Grupo'] == 'com_lavanderia', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {lav1:.2f}')
        lav2 = com_lav.loc[com_lav['Grupo'] == 'com_lavanderia', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{lav2}')
        lav3 = com_lav.loc[com_lav['Grupo'] == 'com_lavanderia', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {lav3:.2f}')
        lav4 = com_lav.loc[com_lav['Grupo'] == 'com_lavanderia', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{lav4}')
        lav5 = com_lav.loc[com_lav['Grupo'] == 'com_lavanderia', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {lav5:.2f}') 
        medias = pd.read_excel('medias.xlsx')
        mlav = medias.loc[medias['Departamento'] == 'com_lavanderia', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mlav:.0f}')
        mlav1= medias.loc[medias['Departamento'] == 'com_lavanderia', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mlav1:.0f}')  
        mlav2= medias.loc[medias['Departamento'] == 'com_lavanderia', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mlav2:.0f}')  
       

    def com_man(self):
        com_man = pd.read_excel('report_por_dpto.xlsx')
        man = com_man.loc[com_man['Grupo'] == 'com_manutencao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{man}')
        man1 = com_man.loc[com_man['Grupo'] == 'com_manutencao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {man1:.2f}')
        man2 = com_man.loc[com_man['Grupo'] == 'com_manutencao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{man2}')
        man3 = com_man.loc[com_man['Grupo'] == 'com_manutencao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {man3:.2f}')
        man4 = com_man.loc[com_man['Grupo'] == 'com_manutencao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{man4}')
        man5 = com_man.loc[com_man['Grupo'] == 'com_manutencao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {man5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mman = medias.loc[medias['Departamento'] == 'com_manutencao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mman:.0f}')
        mman1= medias.loc[medias['Departamento'] == 'com_manutencao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mman1:.0f}')
        mman2= medias.loc[medias['Departamento'] == 'com_manutencao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mman2:.0f}')    

    def com_res(self):
        com_res = pd.read_excel('report_por_dpto.xlsx')
        res = com_res.loc[com_res['Grupo'] == 'com_reservas', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{res}')
        res1 = com_res.loc[com_res['Grupo'] == 'com_reservas', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {res1:.2f}')
        res2 = com_res.loc[com_res['Grupo'] == 'com_reservas', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{res2}')
        res3 = com_res.loc[com_res['Grupo'] == 'com_reservas', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {res3:.2f}')
        res4 = com_res.loc[com_res['Grupo'] == 'com_reservas', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{res4}')
        res5 = com_res.loc[com_res['Grupo'] == 'com_reservas', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {res5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mres = medias.loc[medias['Departamento'] == 'com_reservas', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mres:.0f}')
        mres1= medias.loc[medias['Departamento'] == 'com_reservas', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mres1:.0f}')  
        mres2= medias.loc[medias['Departamento'] == 'com_reservas', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mres2:.0f}')  


    def com_seg(self):
        com_seg = pd.read_excel('report_por_dpto.xlsx')
        seg = com_seg.loc[com_seg['Grupo'] == 'com_seguridad', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{seg}')
        seg1 = com_seg.loc[com_seg['Grupo'] == 'com_seguridad', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {seg1:.2f}')
        seg2 = com_seg.loc[com_seg['Grupo'] == 'com_seguridad', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{seg2}')
        seg3 = com_seg.loc[com_seg['Grupo'] == 'com_seguridad', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {seg3:.2f}')
        seg4 = com_seg.loc[com_seg['Grupo'] == 'com_seguridad', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{seg4}')
        seg5 = com_seg.loc[com_seg['Grupo'] == 'com_seguridad', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {seg5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mseg = medias.loc[medias['Departamento'] == 'com_seguridad', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mseg:.0f}')
        mseg1= medias.loc[medias['Departamento'] == 'com_seguridad', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mseg1:.0f}')  
        mseg2= medias.loc[medias['Departamento'] == 'com_seguridad', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mseg2:.0f}')  



    def com_tel(self):
        com_tel = pd.read_excel('report_por_dpto.xlsx')
        tel = com_tel.loc[com_tel['Grupo'] == 'com_telefones', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{tel}')
        tel1 = com_tel.loc[com_tel['Grupo'] == 'com_telefones', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {tel1:.2f}')
        tel2 = com_tel.loc[com_tel['Grupo'] == 'com_telefones', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{tel2}')
        tel3 = com_tel.loc[com_tel['Grupo'] == 'com_telefones', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {tel3:.2f}')
        tel4 = com_tel.loc[com_tel['Grupo'] == 'com_telefones', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{tel4}')
        tel5 = com_tel.loc[com_tel['Grupo'] == 'com_telefones', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {tel5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mtel = medias.loc[medias['Departamento'] == 'com_telefones', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mtel:.0f}')
        mtel1= medias.loc[medias['Departamento'] == 'com_telefones', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mtel1:.0f}') 
        mtel2= medias.loc[medias['Departamento'] == 'com_telefones', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mtel2:.0f}')  
 


    def h1_anim(self):
        h1_anim = pd.read_excel('report_por_dpto.xlsx')
        anim = h1_anim.loc[h1_anim['Grupo'] == 'h1_animacao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{anim}')
        anim1 = h1_anim.loc[h1_anim['Grupo'] == 'h1_animacao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {anim1:.2f}')
        anim2 = h1_anim.loc[h1_anim['Grupo'] == 'h1_animacao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{anim2}')
        anim3 = h1_anim.loc[h1_anim['Grupo'] == 'h1_animacao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {anim3:.2f}')
        anim4 = h1_anim.loc[h1_anim['Grupo'] == 'h1_animacao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{anim4}')
        anim5 = h1_anim.loc[h1_anim['Grupo'] == 'h1_animacao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {anim5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhanim = medias.loc[medias['Departamento'] == 'h1_animacao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhanim:.0f}')
        mhanim1= medias.loc[medias['Departamento'] == 'h1_animacao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhanim1:.0f}') 
        mhanim2= medias.loc[medias['Departamento'] == 'h1_animacao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhanim2:.0f}')  
 

        
    def h1_bar(self):
        h1_bar = pd.read_excel('report_por_dpto.xlsx')
        bar = h1_bar.loc[h1_bar['Grupo'] == 'h1_bares', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{bar}')
        bar1 = h1_bar.loc[h1_bar['Grupo'] == 'h1_bares', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {bar1:.2f}')
        bar2 = h1_bar.loc[h1_bar['Grupo'] == 'h1_bares', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{bar2}')
        bar3 = h1_bar.loc[h1_bar['Grupo'] == 'h1_bares', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {bar3:.2f}')
        bar4 = h1_bar.loc[h1_bar['Grupo'] == 'h1_bares', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{bar4}')
        bar5 = h1_bar.loc[h1_bar['Grupo'] == 'h1_bares', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {bar5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhbar = medias.loc[medias['Departamento'] == 'h1_bares', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhbar:.0f}')
        mhbar1= medias.loc[medias['Departamento'] == 'h1_bares', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhbar1:.0f}') 
        mhbar2= medias.loc[medias['Departamento'] == 'h1_bares', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhbar2:.0f}')  
 


    def h1_coz(self):
        h1_coz = pd.read_excel('report_por_dpto.xlsx')
        coz = h1_coz.loc[h1_coz['Grupo'] == 'h1_cozinha', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{coz}')
        coz1 = h1_coz.loc[h1_coz['Grupo'] == 'h1_cozinha', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {coz1:.2f}')
        coz2 = h1_coz.loc[h1_coz['Grupo'] == 'h1_cozinha', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{coz2}')
        coz3 = h1_coz.loc[h1_coz['Grupo'] == 'h1_cozinha', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {coz3:.2f}')
        coz4 = h1_coz.loc[h1_coz['Grupo'] == 'h1_cozinha', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{coz4}')
        coz5 = h1_coz.loc[h1_coz['Grupo'] == 'h1_cozinha', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {coz5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhcoz = medias.loc[medias['Departamento'] == 'h1_cozinha', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhcoz:.0f}')
        mhcoz1= medias.loc[medias['Departamento'] == 'h1_cozinha', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhcoz1:.0f}')  
        mhcoz2= medias.loc[medias['Departamento'] == 'h1_cozinha', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhcoz2:.0f}')  
        
    def h1_dir(self):
        h1_dir = pd.read_excel('report_por_dpto.xlsx')
        dir = h1_dir.loc[h1_dir['Grupo'] == 'h1_direcao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{dir}')
        dir1 = h1_dir.loc[h1_dir['Grupo'] == 'h1_direcao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {dir1:.2f}')
        dir2 = h1_dir.loc[h1_dir['Grupo'] == 'h1_direcao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{dir2}')
        dir3 = h1_dir.loc[h1_dir['Grupo'] == 'h1_direcao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {dir3:.2f}')
        dir4 = h1_dir.loc[h1_dir['Grupo'] == 'h1_direcao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{dir4}')
        dir5 = h1_dir.loc[h1_dir['Grupo'] == 'h1_direcao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {dir5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhdir = medias.loc[medias['Departamento'] == 'h1_direcao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhdir:.0f}')
        mhdir1= medias.loc[medias['Departamento'] == 'h1_direcao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhdir1:.0f}')  
        mhdir2= medias.loc[medias['Departamento'] == 'h1_direcao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhdir2:.0f}')  
        
    def h1_gov(self):
        h1_gov = pd.read_excel('report_por_dpto.xlsx')
        gov = h1_gov.loc[h1_gov['Grupo'] == 'h1_governanta', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{gov}')
        gov1 = h1_gov.loc[h1_gov['Grupo'] == 'h1_governanta', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {gov1:.2f}')
        gov2 = h1_gov.loc[h1_gov['Grupo'] == 'h1_governanta', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{gov2}')
        gov3 = h1_gov.loc[h1_gov['Grupo'] == 'h1_governanta', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {gov3:.2f}')
        gov4 = h1_gov.loc[h1_gov['Grupo'] == 'h1_governanta', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{gov4}')
        gov5 = h1_gov.loc[h1_gov['Grupo'] == 'h1_governanta', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {gov5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhgov = medias.loc[medias['Departamento'] == 'h1_governanta', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhgov:.0f}')
        mhgov1= medias.loc[medias['Departamento'] == 'h1_governanta', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhgov1:.0f}')  
        mhgov2= medias.loc[medias['Departamento'] == 'h1_governanta', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhgov2:.0f}')  
          
    def h1_man(self):
        h1_man = pd.read_excel('report_por_dpto.xlsx')
        man = h1_man.loc[h1_man['Grupo'] == 'h1_manutencao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{man}')
        man1 = h1_man.loc[h1_man['Grupo'] == 'h1_manutencao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {man1:.2f}')
        man2 = h1_man.loc[h1_man['Grupo'] == 'h1_manutencao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{man2}')
        man3 = h1_man.loc[h1_man['Grupo'] == 'h1_manutencao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {man3:.2f}')
        man4 = h1_man.loc[h1_man['Grupo'] == 'h1_manutencao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{man4}')
        man5 = h1_man.loc[h1_man['Grupo'] == 'h1_manutencao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {man5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhman = medias.loc[medias['Departamento'] == 'h1_manutencao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhman:.0f}')
        mhman1= medias.loc[medias['Departamento'] == 'h1_manutencao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhman1:.0f}')  
        mhman2= medias.loc[medias['Departamento'] == 'h1_manutencao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhman2:.0f}')          

    def h1_recep(self):
        h1_recep = pd.read_excel('report_por_dpto.xlsx')
        recep = h1_recep.loc[h1_recep['Grupo'] == 'h1_recepcao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{recep}')
        recep1 = h1_recep.loc[h1_recep['Grupo'] == 'h1_recepcao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {recep1:.2f}')
        recep2 = h1_recep.loc[h1_recep['Grupo'] == 'h1_recepcao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{recep2}')
        recep3 = h1_recep.loc[h1_recep['Grupo'] == 'h1_recepcao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {recep3:.2f}')
        recep4 = h1_recep.loc[h1_recep['Grupo'] == 'h1_recepcao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{recep4}')
        recep5 = h1_recep.loc[h1_recep['Grupo'] == 'h1_recepcao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {recep5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mhrecep = medias.loc[medias['Departamento'] == 'h1_recepcao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhrecep:.0f}')
        mhrecep1= medias.loc[medias['Departamento'] == 'h1_recepcao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhrecep1:.0f}')      
        mhrecep2= medias.loc[medias['Departamento'] == 'h1_recepcao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhrecep2:.0f}')      

    def h1_rp(self):
        h1_rp = pd.read_excel('report_por_dpto.xlsx')
        rp = h1_rp.loc[h1_rp['Grupo'] == 'h1_rrpp', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{rp}')
        rp1 = h1_rp.loc[h1_rp['Grupo'] == 'h1_rrpp', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {rp1:.2f}')
        rp2 = h1_rp.loc[h1_rp['Grupo'] == 'h1_rrpp', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{rp2}')
        rp3 = h1_rp.loc[h1_rp['Grupo'] == 'h1_rrpp', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {rp3:.2f}')
        rp4 = h1_rp.loc[h1_rp['Grupo'] == 'h1_rrpp', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{rp4}')
        rp5 = h1_rp.loc[h1_rp['Grupo'] == 'h1_rrpp', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {rp5:.2f}')    
        medias = pd.read_excel('medias.xlsx')
        mhrp = medias.loc[medias['Departamento'] == 'h1_rrpp', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mhrp:.0f}')
        mhrp1= medias.loc[medias['Departamento'] == 'h1_rrpp', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mhrp1:.0f}')  
        mhrp2= medias.loc[medias['Departamento'] == 'h1_rrpp', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mhrp2:.0f}')          


    def h2_anim(self):
        h2_anim = pd.read_excel('report_por_dpto.xlsx')
        anim = h2_anim.loc[h2_anim['Grupo'] == 'h2_animacao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{anim}')
        anim1 = h2_anim.loc[h2_anim['Grupo'] == 'h2_animacao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {anim1:.2f}')
        anim2 = h2_anim.loc[h2_anim['Grupo'] == 'h2_animacao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{anim2}')
        anim3 = h2_anim.loc[h2_anim['Grupo'] == 'h2_animacao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {anim3:.2f}')
        anim4 = h2_anim.loc[h2_anim['Grupo'] == 'h2_animacao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{anim4}')
        anim5 = h2_anim.loc[h2_anim['Grupo'] == 'h2_animacao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {anim5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2anim = medias.loc[medias['Departamento'] == 'h2_animacao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2anim:.0f}')
        mh2anim1= medias.loc[medias['Departamento'] == 'h2_animacao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2anim1:.0f}')
        mh2anim2= medias.loc[medias['Departamento'] == 'h2_animacao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2anim2:.0f}')      
      

        
    def h2_bar(self):
        h2_bar = pd.read_excel('report_por_dpto.xlsx')
        bar = h2_bar.loc[h2_bar['Grupo'] == 'h2_bares', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{bar}')
        bar1 = h2_bar.loc[h2_bar['Grupo'] == 'h2_bares', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {bar1:.2f}')
        bar2 = h2_bar.loc[h2_bar['Grupo'] == 'h2_bares', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{bar2}')
        bar3 = h2_bar.loc[h2_bar['Grupo'] == 'h2_bares', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {bar3:.2f}')
        bar4 = h2_bar.loc[h2_bar['Grupo'] == 'h2_bares', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{bar4}')
        bar5 = h2_bar.loc[h2_bar['Grupo'] == 'h2_bares', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {bar5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2bar = medias.loc[medias['Departamento'] == 'h2_bares', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2bar:.0f}')
        mh2bar1= medias.loc[medias['Departamento'] == 'h2_bares', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2bar1:.0f}')
        mh2bar2= medias.loc[medias['Departamento'] == 'h2_bares', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2bar2:.0f}')            

    def h2_coz(self):
        h2_coz = pd.read_excel('report_por_dpto.xlsx')
        coz = h2_coz.loc[h2_coz['Grupo'] == 'h2_cozinha', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{coz}')
        coz1 = h2_coz.loc[h2_coz['Grupo'] == 'h2_cozinha', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {coz1:.2f}')
        coz2 = h2_coz.loc[h2_coz['Grupo'] == 'h2_cozinha', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{coz2}')
        coz3 = h2_coz.loc[h2_coz['Grupo'] == 'h2_cozinha', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {coz3:.2f}')
        coz4 = h2_coz.loc[h2_coz['Grupo'] == 'h2_cozinha', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{coz4}')
        coz5 = h2_coz.loc[h2_coz['Grupo'] == 'h2_cozinha', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {coz5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2coz = medias.loc[medias['Departamento'] == 'h2_cozinha', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2coz:.0f}')
        mh2coz1= medias.loc[medias['Departamento'] == 'h2_cozinha', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2coz1:.0f}')    
        mh2coz2= medias.loc[medias['Departamento'] == 'h2_cozinha', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2coz2:.0f}')      
  

        
    def h2_dir(self):
        h2_dir = pd.read_excel('report_por_dpto.xlsx')
        dir = h2_dir.loc[h2_dir['Grupo'] == 'h2_direcao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{dir}')
        dir1 = h2_dir.loc[h2_dir['Grupo'] == 'h2_direcao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {dir1:.2f}')
        dir2 = h2_dir.loc[h2_dir['Grupo'] == 'h2_direcao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{dir2}')
        dir3 = h2_dir.loc[h2_dir['Grupo'] == 'h2_direcao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {dir3:.2f}')
        dir4 = h2_dir.loc[h2_dir['Grupo'] == 'h2_direcao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{dir4}')
        dir5 = h2_dir.loc[h2_dir['Grupo'] == 'h2_direcao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {dir5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2dir = medias.loc[medias['Departamento'] == 'h2_direcao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2dir:.0f}')
        mh2dir1= medias.loc[medias['Departamento'] == 'h2_direcao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2dir1:.0f}')    
        mh2dir2= medias.loc[medias['Departamento'] == 'h2_direcao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2dir2:.0f}')        


    def h2_gov(self):
        h2_gov = pd.read_excel('report_por_dpto.xlsx')
        gov = h2_gov.loc[h2_gov['Grupo'] == 'h2_governanta', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{gov}')
        gov1 = h2_gov.loc[h2_gov['Grupo'] == 'h2_governanta', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {gov1:.2f}')
        gov2 = h2_gov.loc[h2_gov['Grupo'] == 'h2_governanta', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{gov2}')
        gov3 = h2_gov.loc[h2_gov['Grupo'] == 'h2_governanta', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {gov3:.2f}')
        gov4 = h2_gov.loc[h2_gov['Grupo'] == 'h2_governanta', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{gov4}')
        gov5 = h2_gov.loc[h2_gov['Grupo'] == 'h2_governanta', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {gov5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2gov = medias.loc[medias['Departamento'] == 'h2_governanta', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2gov:.0f}')
        mh2gov1= medias.loc[medias['Departamento'] == 'h2_governanta', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2gov1:.0f}') 
        mh2gov2= medias.loc[medias['Departamento'] == 'h2_governanta', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2gov2:.0f}')      
     

    def h2_man(self):
        h2_man = pd.read_excel('report_por_dpto.xlsx')
        man = h2_man.loc[h2_man['Grupo'] == 'h2_manutencao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{man}')
        man1 = h2_man.loc[h2_man['Grupo'] == 'h2_manutencao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {man1:.2f}')
        man2 = h2_man.loc[h2_man['Grupo'] == 'h2_manutencao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{man2}')
        man3 = h2_man.loc[h2_man['Grupo'] == 'h2_manutencao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {man3:.2f}')
        man4 = h2_man.loc[h2_man['Grupo'] == 'h2_manutencao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{man4}')
        man5 = h2_man.loc[h2_man['Grupo'] == 'h2_manutencao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {man5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2man = medias.loc[medias['Departamento'] == 'h2_manutencao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2man:.0f}')
        mh2man1= medias.loc[medias['Departamento'] == 'h2_manutencao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2man1:.0f}')    
        mh2man2= medias.loc[medias['Departamento'] == 'h2_manutencao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2man2:.0f}')        
            
    def h2_recep(self):
        h2_recep = pd.read_excel('report_por_dpto.xlsx')
        recep = h2_recep.loc[h2_recep['Grupo'] == 'h2_recepcao', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{recep}')
        recep1 = h2_recep.loc[h2_recep['Grupo'] == 'h2_recepcao', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {recep1:.2f}')
        recep2 = h2_recep.loc[h2_recep['Grupo'] == 'h2_recepcao', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{recep2}')
        recep3 = h2_recep.loc[h2_recep['Grupo'] == 'h2_recepcao', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {recep3:.2f}')
        recep4 = h2_recep.loc[h2_recep['Grupo'] == 'h2_recepcao', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{recep4}')
        recep5 = h2_recep.loc[h2_recep['Grupo'] == 'h2_recepcao', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {recep5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2recep = medias.loc[medias['Departamento'] == 'h2_recepcao', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2recep:.0f}')
        mh2recep1= medias.loc[medias['Departamento'] == 'h2_recepcao', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2recep1:.0f}') 
        mh2recep2= medias.loc[medias['Departamento'] == 'h2_recepcao', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2recep2:.0f}')      
             
        
    def h2_rp(self):
        h2_rp = pd.read_excel('report_por_dpto.xlsx')
        rp = h2_rp.loc[h2_rp['Grupo'] == 'h2_rrpp', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{rp}')
        rp1 = h2_rp.loc[h2_rp['Grupo'] == 'h2_rrpp', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {rp1:.2f}')
        rp2 = h2_rp.loc[h2_rp['Grupo'] == 'h2_rrpp', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{rp2}')
        rp3 = h2_rp.loc[h2_rp['Grupo'] == 'h2_rrpp', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {rp3:.2f}')
        rp4 = h2_rp.loc[h2_rp['Grupo'] == 'h2_rrpp', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{rp4}')
        rp5 = h2_rp.loc[h2_rp['Grupo'] == 'h2_rrpp', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {rp5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mh2rp = medias.loc[medias['Departamento'] == 'h2_rrpp', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mh2rp:.0f}')
        mh2rp1= medias.loc[medias['Departamento'] == 'h2_rrpp', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mh2rp1:.0f}')  
        mh2rp2= medias.loc[medias['Departamento'] == 'h2_rrpp', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mh2rp2:.0f}')          
        

    def com_rh(self):
        rrhh = pd.read_excel('report_por_dpto.xlsx')
        com_rrhh = rrhh.loc[rrhh['Grupo'] == 'com_enfermaria', 'Páginas coloridas'].values[0]
        h1_rrhh = rrhh.loc[rrhh['Grupo'] == 'com_rrhh', 'Páginas coloridas'].values[0]
        soma_cor_rrhh = com_rrhh + h1_rrhh
        self.root.ids.cor_total.text = (f'{soma_cor_rrhh}')
        com_rrhh1 = rrhh.loc[rrhh['Grupo'] == 'com_enfermaria', 'Custo Coloridas'].values[0]
        h1_rrhh1 = rrhh.loc[rrhh['Grupo'] == 'com_rrhh', 'Custo Coloridas'].values[0]
        soma_cor_rrhh1 = com_rrhh1 + h1_rrhh1
        self.root.ids.cor_custo.text = (f'{soma_cor_rrhh1:.2f}')
        com_rrhh2 = rrhh.loc[rrhh['Grupo'] == 'com_enfermaria', 'Páginas Escala de Cinza'].values[0]
        h1_rrhh2 = rrhh.loc[rrhh['Grupo'] == 'com_rrhh', 'Páginas Escala de Cinza'].values[0]
        soma_cor_rrhh2 = com_rrhh2 + h1_rrhh2
        self.root.ids.pb_total.text = (f'{soma_cor_rrhh2}')
        com_rrhh3 = rrhh.loc[rrhh['Grupo'] == 'com_enfermaria', 'Custo P & B'].values[0]
        h1_rrhh3 = rrhh.loc[rrhh['Grupo'] == 'com_rrhh', 'Custo P & B'].values[0]
        soma_cor_rrhh3 = com_rrhh3 + h1_rrhh3
        self.root.ids.pb_custo.text = (f'{soma_cor_rrhh3:.2f}')
        com_rrhh4 = rrhh.loc[rrhh['Grupo'] == 'com_enfermaria', 'Total Páginas impressas'].values[0]
        h1_rrhh4 = rrhh.loc[rrhh['Grupo'] == 'com_rrhh', 'Total Páginas impressas'].values[0]
        soma_cor_rrhh4 = com_rrhh4 + h1_rrhh4
        self.root.ids.total_dpto.text = (f'{soma_cor_rrhh4}')
        com_rrhh5 = rrhh.loc[rrhh['Grupo'] == 'com_enfermaria', 'Custo Departamento'].values[0]
        h1_rrhh5 = rrhh.loc[rrhh['Grupo'] == 'com_rrhh', 'Custo Departamento'].values[0]
        soma_cor_rrhh5 = com_rrhh5 + h1_rrhh5
        self.root.ids.custo_dpto.text = (f'{soma_cor_rrhh5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        mrh = medias.loc[medias['Departamento'] == 'com_rrhh', 2019].values[0]
        self.root.ids.media_2019.text = (f'{mrh:.0f}')
        mrh1= medias.loc[medias['Departamento'] == 'com_rrhh', 2020].values[0]
        self.root.ids.media_2020.text = (f'{mrh1:.0f}')     
        mrh2= medias.loc[medias['Departamento'] == 'com_rrhh', 2021].values[0]
        self.root.ids.media_2021.text = (f'{mrh2:.0f}')       
        

    def salvador(self):
        salvador = pd.read_excel('report_por_dpto.xlsx')
        salv = salvador.loc[salvador['Grupo'] == 'com_Escritório_Salvador', 'Páginas coloridas'].values[0]
        self.root.ids.cor_total.text = (f'{salv}')
        salv1 = salvador.loc[salvador['Grupo'] == 'com_Escritório_Salvador', 'Custo Coloridas'].values[0]
        self.root.ids.cor_custo.text = (f'R$ {salv1:.2f}')
        salv2 = salvador.loc[salvador['Grupo'] == 'com_Escritório_Salvador', 'Páginas Escala de Cinza'].values[0]
        self.root.ids.pb_total.text = (f'{salv2}')
        salv3 = salvador.loc[salvador['Grupo'] == 'com_Escritório_Salvador', 'Custo P & B'].values[0]
        self.root.ids.pb_custo.text = (f'R$ {salv3:.2f}')
        salv4 = salvador.loc[salvador['Grupo'] == 'com_Escritório_Salvador', 'Total Páginas impressas'].values[0]
        self.root.ids.total_dpto.text = (f'{salv4}')
        salv5 = salvador.loc[salvador['Grupo'] == 'com_Escritório_Salvador', 'Custo Departamento'].values[0]
        self.root.ids.custo_dpto.text = (f'R$ {salv5:.2f}')
        medias = pd.read_excel('medias.xlsx')
        msalv = medias.loc[medias['Departamento'] == 'com_Escritório_Salvador', 2019].values[0]
        self.root.ids.media_2019.text = (f'{msalv:.0f}')
        msalv1= medias.loc[medias['Departamento'] == 'com_Escritório_Salvador', 2020].values[0]
        self.root.ids.media_2020.text = (f'{msalv1:.0f}') 
        msalv2= medias.loc[medias['Departamento'] == 'com_Escritório_Salvador', 2021].values[0]
        self.root.ids.media_2021.text = (f'{msalv2:.0f}') 
 

    

            
   
   
  


    #CONSTRUTOR DO APP
    def build(self):
        return Builder.load_string(KV)


Report_Printer().run()