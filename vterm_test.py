#!/usr/bin/python
#
# Urwid terminal emulation widget example app
#    Copyright (C) 2010  aszlig
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Urwid web site: http://excess.org/urwid/

import urwid

def main():
    event_loop = urwid.SelectEventLoop()

    mainframe = urwid.Frame(
        urwid.Columns([
            ('fixed', 3, urwid.SolidFill('|')),
            urwid.Pile([
                ('weight', 70, urwid.TerminalWidget(None, event_loop)),
                ('fixed', 1, urwid.Filler(urwid.Edit('focus test edit: '))),
            ]),
            ('fixed', 3, urwid.SolidFill('|')),
        ], box_columns=[1]),
        header=urwid.Columns([
            ('fixed', 3, urwid.Text('.,:')),
            urwid.Divider('-'),
            ('fixed', 3, urwid.Text(':,.')),
        ]),
        footer=urwid.Columns([
            ('fixed', 3, urwid.Text('`"*')),
            urwid.Divider('-'),
            ('fixed', 3, urwid.Text('*"\'')),
        ]),
    )

    def quit(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    loop = urwid.MainLoop(
        mainframe,
        handle_mouse=False,
        unhandled_input=quit,
        event_loop=event_loop
    ).run()

if __name__ == '__main__':
    main()
