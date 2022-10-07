import dearpygui.dearpygui as dpg
import installer, settings, logger, sys, os, winsound

def startJavaInstall(bitness, custompath, path):
    javainstallcore = installer.JavaInstaller(bittnes=bitness,custompath=custompath,path=path)
    javainstallcore.install()

def startLauncherInstall():
    launcherinstallcore = installer.LauncherInstaller()
    launcherinstallcore.install()

def inst_callback():
    if dpg.is_item_enabled("but"):
        logger.addLogData('Start Install '+settings.project_name)
        if settings.dev:
            logger.addLogDataDebug(dpg.get_value("checkbox"))
            if dpg.does_item_exist("path"):
                logger.addLogDataDebug(dpg.get_value("path"))
            logger.addLogDataDebug(dpg.get_value("bitness"))
        bitness = "None"
        if dpg.get_value("bitness") == "x64":
            bitness = "64"
        elif dpg.get_value("bitness") == "x86":
            bitness = "86"
        else:
            logger.addLogDataError("Wrong bitness")
            pass
        if dpg.get_value("checkbox"):
            if not dpg.does_item_exist("path"):
                logger.addLogDataError("Application broken")
                pass
            path = dpg.get_value("path")
        else:
            path = ""
        startJavaInstall(bitness,dpg.get_value("checkbox"),path)
        startLauncherInstall()
        logger.addLogDataSuccess(settings.project_name+" is installed successfully!")
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        dpg.disable_item("but")




def checkbox():
    if not dpg.get_value("checkbox"):
        dpg.disable_item("path")
        dpg.delete_item("path")
    else:
        if not dpg.does_item_exist("path"):
            if dpg.get_value("bitness") == "x64":
                dpg.add_input_text(parent="Installation",tag="path", label="Path for Java", default_value=settings.java_64_custompath_example, enabled=False,before ="but")
            elif dpg.get_value("bitness") == "x86":
                dpg.add_input_text(parent="Installation", tag="path", label="Path for Java",default_value=settings.java_32_custompath_example, enabled=False, before="but")
        dpg.enable_item("path")

dpg.create_context()

with dpg.window(tag="Installation"):
    dpg.add_text("Installation "+settings.project_name)
    dpg.add_text("Bitness:")
    dpg.add_listbox(tag="bitness",items=['x64','x86'],num_items=1)
    dpg.add_checkbox(tag="checkbox",label="Custom part for Java", callback=checkbox,default_value=False)
    #dpg.add_input_text(parent="Installation",tag="path" ,label="Path for Java",default_value='C:\Program Files\Java',enabled=False,before ="but")
    dpg.add_button(tag="but" ,label="Install", callback=inst_callback)
    dpg.add_text("Log:")
    dpg.add_input_text(multiline=True,tag="log",width=450)
    with dpg.menu_bar():
        with dpg.menu(label="About"):
            dpg.add_text('SIMPLE INSTALLER v0.0.1a\nCopyright MCProjectX © 2022')
with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, [180, 50, 211])
dpg.bind_theme(global_theme)
#dpg.show_style_editor()
if settings.dev:
    dpg.create_viewport(title=settings.program_title, width=500, max_height=340,resizable=False,small_icon="favicon.ico",large_icon="favicon.ico")
else:
    dpg.create_viewport(title=settings.program_title, width=500, max_height=340,resizable=False,small_icon=os.path.join(sys._MEIPASS, "files/favicon.ico"),large_icon=os.path.join(sys._MEIPASS, "files/favicon.ico"))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Installation", True)
dpg.start_dearpygui()

dpg.destroy_context()
