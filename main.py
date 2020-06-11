from Vue.root_frame import RootFrame


def main():

    # init vue
    root = RootFrame()
    root.master.title("ZoZan Kebab")
    root.show_menu()

    # start
    root.mainloop()

if __name__ == "__main__":
    main()