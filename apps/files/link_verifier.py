import re


class LinkVerifier():
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  
    def __init__(self, checked_link) -> None:
        self.checked_link = checked_link

    def link_is_valid(self) -> bool:
        return (re.match(LinkVerifier.regex,
                         self.checked_link) is not None)


if __name__ == '__main__':
    print(LinkVerifier('http://www.example.com').link_is_valid())
    print(LinkVerifier('http://www.exa2ц34234234mplcom').link_is_valid())
    print(LinkVerifier('example.com').link_is_valid())
