TYPE_OS = 2  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            dlg = super().__new__(DialogWindows)
            name = args[0]
            setattr(dlg, "name", name)
            return dlg
        elif TYPE_OS == 2:
            dlg = super().__new__(DialogLinux)
            name = args[0]
            setattr(dlg, "name", name)
            return dlg

    #    else:
    #        dlg = super().__new__(cls)
    #        return dlg

    #    def __init__(self, name):
    #        self.name = name


print(Dialog("dialog").name)
