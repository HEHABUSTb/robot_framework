import subprocess
import time
import logging
import socket


"""
Для работы в переменных должен быть прописан путь до Android-sdk и platform-tools, запущен adb start-server
"""


class Emulator:

    def __init__(self):
        self.pc_name = self.get_computer_name()

    @staticmethod
    def get_computer_name():
        pc_name = socket.gethostname()
        return pc_name

    def start_android_emulator(self):
        if self.pc_name == 'LT-024-01':
            emulator_path = r'C:\Users\a.liubinskii\AppData\Local\Android\Sdk\emulator\emulator.exe'
            avd_name = 'Pixel_2'

            logging.info("Launching adb server")
            cmd = r"adb start-server"
            subprocess.Popen(cmd)
            time.sleep(5)

        elif self.pc_name == 'LT002-01.local':
            emulator_path = r'/Users/build_user/Library/Android/sdk/emulator/emulator'
            avd_name = 'Pixel_2'

            logging.info("Launching adb server")
            cmd = 'bash -c "adb start-server"'
            subprocess.Popen(cmd, shell=True)

        else:
            raise AssertionError(f"Emulator path and device name is not defined for {self.pc_name} check Emulator.py")

        logging.info(f"Launching emulator device {avd_name}")
        cmd = [emulator_path, '-avd', avd_name]
        subprocess.Popen(cmd)
        time.sleep(20)

    def stop_android_emulator(self):

        logging.info('Stopping emulator')
        cmd = r"adb -s emulator-5554 emu kill"
        if self.pc_name == 'LT002-01.local':
            cmd = 'bash -c "adb -s emulator-5554 emu kill"'
        subprocess.Popen(cmd, shell=True)
        time.sleep(20)


if __name__ == '__main__':
    emu = Emulator()
    emu.start_android_emulator()
