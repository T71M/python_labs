

def main():
    list = ["www.git", "www.vk", "youtube.com"]
    outputList = []
    for link in list:
        if len(link) >= 4:
            string = link[0:3]
            if string == "www":
                link = "http:/" + link
                string = link[-1:-5]
                if string != ".com":
                    link += ".com"
                outputList.append(link)
    print(outputList)


if __name__ == "__main__":
    main()
