#!/usr/bin/env python2
import subprocess

from config import attached_icon, dettached_icon, execute_str

def output_menu_entry(tinfo):

    label = "{} ({})".format(tinfo['name'], tinfo['num'])
    execute = execute_str.format(tinfo['name'], tinfo['attached'])

    if tinfo['attached']:
        icon = attached_icon
    else:
        icon = dettached_icon 

    print '<item label="{}" icon="{}">'.format(label, icon)
    print '  <action name="Execute">'
    print '    <command>'+execute+'</command>'
    print '  </action>'
    print '</item>'

def get_tmux_info():
    output = subprocess.check_output(['tmux', 'ls'])
    tmux_windows = []
    for t in output.splitlines():
        tinfo = {}
        tinfo['name'] = t.split(':')[0]
        tinfo['num'] = t.split(':')[1].strip().split(' ')[0]
        at = t.split(' ')[-1]
        if at == '(attached)':
            tinfo['attached'] = True
        else:
            tinfo['attached'] = False
        tmux_windows.append(tinfo)
    return tmux_windows

if __name__ == '__main__':
    print '<openbox_pipe_menu>'
    print '<separator label="Tmux Windows" />'
    for tinfo in get_tmux_info():
        output_menu_entry(tinfo)
    print '</openbox_pipe_menu>'
