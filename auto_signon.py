from pywinauto import Desktop
from pywinauto.application import Application

d = Desktop(backend='uia')

# d['작업 표시줄'].dump_tree()
main_tray_toolbar = d['작업 표시줄'].child_window(title="사용자 지정 알림 영역", control_type="ToolBar")

# print(main_tray_toolbar.texts())
icon = main_tray_toolbar.child_window(title_re="CreonPlus Start", control_type="Button")
icon.click_input(button="right")  # 트레이 아이콘 마우스 우 클릭

# d['컨텍스트Menu'].dump_tree()
icon2 = d['컨텍스트Menu'].child_window(title="복수계좌 사인온 변경", control_type="MenuItem")
icon2.click_input(button='left')  # 사인온 버튼 클릭

app = Application(backend="uia").connect(path="C:\\DAISHIN\\CYBOSPLUS\\CpStart.exe")
diag = app.window(title="복수계좌 사인온 변경")
diag['사인온'].click()
