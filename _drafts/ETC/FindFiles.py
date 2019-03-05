import os

def find_a_kind_of_file(root, which_ext):
    for (path, dir, files) in os.walk(root):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == which_ext:
                # print("%s/%s" % (path, filename))
                print("%s" % (filename))

if __name__ == '__main__':
    print("This program show you the list of files.")
    # root = input("Please, input the root directory for search.");
    # which_ext = input("Please, input an extension for search");
    root = "/Users/psj/Desktop/fnhero-android_tudalapp/app/src/main/java/in/tudal/app"
    which_ext = ".java"
    find_a_kind_of_file(root, which_ext);
