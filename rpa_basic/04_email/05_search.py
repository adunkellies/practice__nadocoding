from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# mailbox.logout()

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 다 가져오기
    # for msg in mailbox.fetch():
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(FROM adunkellies@gmail.com)', limit=3, reverse=True): # 특정인이 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요
    # 어떤 글자를 포함하는 메일 (제목, 분문), 띄어쓰기로 구분하여 "test", "mail" 이라는 각각의 단어를 포함하는 메일을 찾게 됨
    # for msg in mailbox.fetch('(TEXT "test mail")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자를 포함하는 메일 (제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자(한글)를 포함하는 메일 필터링 (제목만)
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 05-Nov-2023)', limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 05-Nov-2023)', limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일 (그리고 조건)
    # for msg in mailbox.fetch('(ON 05-Nov-2023 SUBJECT "test mail")', limit=5,reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건 중 하나라도 만족하는 메일 (또는 조건)
    for msg in mailbox.fetch('(OR ON 05-Nov-2023 SUBJECT "test mail")', limit=5,reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))