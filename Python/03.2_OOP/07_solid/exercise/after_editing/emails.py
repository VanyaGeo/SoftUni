from abc import ABC, abstractmethod


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def format_sender(self):
        pass


class IReceiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def format_receiver(self):
        pass


class IContent(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format_content(self):
        pass


class MyContent(ISender, IReceiver, IContent):
    def __init__(self, sender, receiver, content):
        ISender.__init__(self, sender)
        IReceiver.__init__(self, receiver)
        IContent.__init__(self, content)

    def format_sender(self):
        return f"I'm {self.sender}"

    def format_receiver(self):
        return f"I'm {self.receiver}"

    def format_content(self):
        return f"<MyML>{self.content}<MyML>"


class IEmail(ABC):
    def __int__(self):
        pass

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = sender.format_sender()
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = receiver.format_receiver()
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format_content()

    def __repr__(self):
        template = f"Sender: {self.__sender}\n" \
                   f"Receiver: {self.__receiver}\n" \
                   f"Content:\n{self.__content}"

        return template


email = Email('IM')
info = MyContent('qmal', 'james', 'Hello, there!')
email.set_sender(info)
email.set_receiver(info)
email.set_content(info)
print(email)
