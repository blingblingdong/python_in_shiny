from shiny import App, render, ui,reactive
from htmltools import HTML, div


page_header=ui.tags.nav(
  {"class": "navbar navbar-inverse"}, 
  ui.tags.div(
  {"class": "container-fluid"}, 
   ui.tags.div(
      {"class": "navbar-brand"}, 
      HTML("<a class='navbar-brand'>聊天機器人</a>")),
   ui.tags.ul(
     {"class": "nav navbar-nav"},
     HTML("<li><a class='active' href='https://lsysocute.shinyapps.io/shinyrobot/'>對話機器人</a></li>"),
     HTML("<li><a class='active' href='https://github.com/blingblingdong/python_in_shiny'><span class='glyphicon glyphicon-info-sign'></span> 查看原始碼</a></li>"),
     HTML("<li><a class='active' href='https://rpubs.com/lsysocute/shiny-robot'><span class='glyphicon glyphicon-thumbs-up'></span>介紹簡報</a></li>")
   )
        )
   )

app_ui = ui.page_fluid(
    ui.tags.style(
        """
        .action-button {height: 40px;width: 80px;color: white;padding: 0px 10px;background-color: #F3E3F8;color: black;border: 0.1px solid white;}
        .form-control {width: 250px;height: 40px}
        .custom-row {display: flex;}  
        .sidebar-content {background-color: pink;}
        .shiny-bound-output{font-size: 18px;}
        #u_in3 input{background-color: pink;border: 1px solid white;}
        #x1 {background-color: #E2E7FD;border: 1px solid black;}
        """
    ),
    page_header,
    ui.layout_sidebar(
      ui.panel_sidebar(
         ui.input_switch("x1", "禮貌版本", False),
         ui.p("請問您的名字是？"),
         ui.div(
           {"class": "custom-row"}, 
           ui.input_text("u_in1","", placeholder="完整姓名"),
           ui.input_action_button("c1","",icon=HTML("<i class='glyphicon glyphicon-send'></i>"))
         ),
         ui.p("請問您的生日是？"),
         ui.div(
           {"class": "custom-row"}, 
         ui.input_text("u_in2", "", placeholder="month/day"),
         ui.input_action_button("c2", "",icon=HTML("<i class='glyphicon glyphicon-send'></i>"))
         ),
         ui.p("你的心情好嗎"),
         ui.div(
           {"class": "custom-row"},
         ui.input_radio_buttons("u_in3","", ["好", "不好"]),
         ui.input_action_button("c3", "",icon=HTML("<i class='glyphicon glyphicon-send'></i>"))
         )
      ),

      ui.panel_main(
        ui.output_text("u_out1"),
        ui.output_text("c_out1"),
        ui.br(),
        ui.output_text("u_out2"),
        ui.output_text("c_out2"),
        ui.br(),
        ui.output_text("u_out3"),
        ui.output_text("c_out3")
    ),
  ),
)

def server(input, output, session):
  
    @output
    @render.text
    def u_out1():
        return f"用戶輸入:我的名字是 {input.u_in1()}"
      
    @output
    @render.text 
    @reactive.event(input.c1)
    def c_out1():
        if input.x1()==True:
            return f"機器人: {input.u_in1()}？這個名字真好聽，很高興今天能跟你聊天！"
        elif input.x1()==False:
            return f"機器人: {input.u_in1()}？恩，我下次就會忘了"
      
    @output
    @render.text
    def u_out2():
        return f"用戶輸入: 我的生日是{input.u_in2()}"
      
    @output
    @render.text 
    @reactive.event(input.c2)
    def c_out2(): 
        if input.x1()==True:
            return f"機器人: 我也是在{input.u_in2()}這天生日誒，太巧了吧"
        elif input.x1()==False:
            return f"機器人: {input.u_in2()}？很快你就要再老一歲啦"
      
    @output
    @render.text
    def u_out3():
        return f"用戶輸入: 我今天心情{input.u_in3()}"
  
    @output
    @render.text 
    @reactive.event(input.c3)
    def c_out3(): 
        if (input.u_in3()== "好")and(input.x1()==True):
            return f"機器人: 太好了！保持正向"
        elif (input.u_in3() == "不好")and(input.x1()==True):
            return f"沒事的，雨過竹筍生，剪不斷理還亂"
        elif (input.u_in3() == "好")and(input.x1()==False):
            return f"看你到期中還笑的笑不出來"
        elif (input.u_in3() == "不好")and(input.x1()==False):
            return f"垂頭喪氣，自憐自艾，少在那邊享受悲情的人設"
        
  
app = App(app_ui, server)


