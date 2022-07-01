from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message=" If you have gained enough knowledge about the Python programming language and want to get selected in any company at a good salary, this video. ",
            app_icon="E:/upload path icon",
            timeout=5)
        time.sleep(10)