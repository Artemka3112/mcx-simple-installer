
# при False не будет собираться лаунчер в среде. Только через ".\build.bat" в терминале.
# True запускает лаунчер без установки файлов и программ(для настройки дизайна кнопок и тп)
dev = False


program_title = "Gravit Launcher Installer"
project_name = "Mc.Ground Project"

launcher_url = "https://launcher.mcground.ru/Launcher.exe" # ссылка на лаунчер
launcher_file_name = "Launcher_test.exe" # имя файла лаунчера на рабочем столе

java_32_url = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=246806_424b9da4b48848379167015dcc250d8d"# ссылка установщик для x86
java_64_url = "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=246808_424b9da4b48848379167015dcc250d8d"# ссылка установщик для x64
java_32_file_name = "jre-windows-x86.exe"# название файла после распаковки(не нужно трогать)
java_64_file_name = "jre-windows-x64.exe"# название файла после распаковки(не нужно трогать)
java_opt = "AUTO_UPDATE=Disable INSTALL_SILENT=Enable STATIC=Enable REBOOT=Disable WEB_ANALYTICS=Disable"# параметры установки java
# Установка Java осуществляется через параметр INSTALLCFG. То-есть параметры из java_opt кладутся в файлик перед запуском установщика Java.