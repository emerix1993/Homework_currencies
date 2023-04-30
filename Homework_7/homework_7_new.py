from dataclasses import dataclass
from abc import ABC, abstractmethod
import datetime


@dataclass
class Post:
    text: str
    timestamp: str


@dataclass
class Prepost:
    text: str


class SocialChannel(ABC):
    def __init__(self, type_social, followers):
        self.type_social = type_social
        self.followers = followers
        self.posts = []
        self.prepost = []

    # @abstractmethod
    def post_message(self, text):
        pass

    # @abstractmethod
    def prepost_message(self, text):
        return self.prepost

    # @abstractmethod
    def get_post(self):
        return self.posts

    # @abstractmethod
    def get_prepost(self):
        return self.prepost

    # @abstractmethod
    def delete_prepost_message(self, text):
        pass

    # @abstractmethod
    def edit_prepost(self, text, new_text):
        pass

    # @abstractmethod
    def intermediate_stage(self, text):
        pass

    @abstractmethod
    def get_followers(self):
        return self.followers


class Facebook(SocialChannel):
    def __init__(self, type_social, followers):
        super().__init__(type_social, followers)

    def prepost_message(self, text):
        facebook_list_message = Prepost(text=text)
        self.prepost.append(facebook_list_message)
        print(self.prepost)
        return "Valid add"

    def delete_prepost_message(self, text):
        self.prepost.remove(Prepost(text=text))
        return "Valid delete"

    def delete_index_message(self, index):
        self.prepost.pop(index)
        return "Valid delete"

    def edit_prepost(self, text, new_text):
        prepost = Prepost(text=text)
        index = self.prepost.index(prepost)
        self.prepost[index] = Prepost(text=new_text)
        return "Valid edit"

    def intermediate_stage(self, text):
        prepost_index = self.prepost.index(Prepost(text=text))
        prepost = self.prepost[prepost_index]
        self.post_message(prepost.text)
        self.delete_prepost_message(prepost.text)
        return "Valid post"

    def post_message(self, text):
        facebook_message = Post(text=text, timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.posts.append(facebook_message)
        return f"New message in facebook: {text}"

    def get_followers(self):
        return self.followers


class Twitter(SocialChannel):
    def __init__(self, type_social, followers):
        super().__init__(type_social, followers)

    def post_message(self, text):
        twitter_message = Post(text=text, timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.posts.append(twitter_message)
        return f"New message in twitter: {text}"

    def prepost_message(self, text):
        twitter_list_message = Prepost(text=text)
        self.prepost.append(twitter_list_message)
        print(self.prepost)
        return "Valid add"

    def delete_prepost_message(self, text):
        self.prepost.remove(Prepost(text=text))
        return "Valid delete"

    def delete_index_message(self, index):
        self.prepost.pop(index)
        return "Valid delete"

    def edit_prepost(self, text, new_text):
        prepost = Prepost(text=text)
        index = self.prepost.index(prepost)
        self.prepost[index] = Prepost(text=new_text)
        return "Valid edit"

    def intermediate_stage(self, text):
        prepost_index = self.prepost.index(Prepost(text=text))
        prepost = self.prepost[prepost_index]
        self.post_message(prepost.text)
        self.delete_prepost_message(prepost.text)
        return "Valid post"

    def get_followers(self):
        return self.followers


class Youtube(SocialChannel):
    def __init__(self, type_social, followers):
        super().__init__(type_social, followers)

    def post_message(self, text):
        youtube_message = Post(text=text, timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.posts.append(youtube_message)
        return f"New message in youtube: {text}"


def main():
    facebook = Facebook(type_social="social network", followers=100)
    twitter = Twitter(type_social="social network", followers=200)
    while True:
        type_social = input("Enter social network: ")
        if type_social == "facebook":
            action = input("Enter you action: ")
            if action == "fall":
                print("bla")
            if action == "create":
                message = input("Enter you message: ")
                print(facebook.post_message(text=message))
            elif action == "create prepost":
                message = input("Enter you message: ")
                print(facebook.prepost_message(text=message))
            elif action == "del":
                message = input("Enter you message for delete: ")
                print(facebook.delete_prepost_message(message))
                print(facebook.get_prepost())
            elif action == "index del":
                index = int(input("Enter you index for delete: "))
                print(facebook.delete_index_message(index))
                print(facebook.get_prepost())
            elif action == "edit":
                text = input("Enter text: ")
                new_text = input("Enter new text: ")
                print(facebook.edit_prepost(text, new_text))
                print(facebook.get_prepost())
            elif action == "list":
                print(facebook.get_post())
            elif action == "prepost":
                print(facebook.get_prepost())
            elif action == "add post":
                text = input("Enter message text: ")
                print(facebook.intermediate_stage(text=text))
            elif action == "followers":
                print(facebook.get_followers())
        elif type_social == "twitter":
            action = input("Enter you action: ")
            if action == "create":
                message = input("Enter you message: ")
                print(twitter.post_message(text=message))
            elif action == "create prepost":
                message = input("Enter you message: ")
                print(twitter.prepost_message(text=message))
            elif action == "del":
                message = input("Enter you message for delete: ")
                print(twitter.delete_prepost_message(message))
                print(twitter.get_prepost())
            elif action == "index del":
                index = int(input("Enter you index for delete: "))
                print(twitter.delete_index_message(index))
                print(twitter.get_prepost())
            elif action == "edit":
                text = input("Enter text: ")
                new_text = input("Enter new text: ")
                print(twitter.edit_prepost(text, new_text))
                print(twitter.get_prepost())
            elif action == "list":
                print(twitter.get_post())
            elif action == "prepost":
                print(twitter.get_prepost())
            elif action == "add post":
                text = input("Enter message text: ")
                print(twitter.intermediate_stage(text=text))
            elif action == "followers":
                print(twitter.get_followers())
        elif type_social == "youtube":
            message = input("Enter you message: ")
            print(youtube.post_message(text=message))
            print(youtube.get_post())


if __name__ == "__main__":
    main()
