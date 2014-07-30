import os
import sys
import subprocess
import sublime
import sublime_plugin


class MarkedCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)

        # NOTE: v2 of Marked uses app name "Marked 2"
        for appName in ['Marked', 'Marked 2']:
            res = subprocess.call(['open', '-a', appName, filename], env=proc_env)
            if res == 0:
                return

    def is_enabled(self):
        return True
