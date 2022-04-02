#!/usr/bin/python3
import gi
gi.require_version("Gtk", "3.0")

import subprocess
from gi.repository import Gtk
from gi.repository import GLib
#from gi.repository import GObject

import os
from subprocess import Popen, PIPE
import fcntl

class Wifite2UI( Gtk.Window ):
    prepped = False
    attacking = False
    grid = Gtk.Grid()
    lblTerminal = Gtk.Label()
    proc = Popen("ping -c10 localhost", stdout=PIPE, shell=True)

    def __init__(self):
        super().__init__( title="Wifite2 UI" )
        self.set_border_width( 10 )

        #grid = Gtk.Grid()

        # add buttons
        btnPrepare = Gtk.Button.new_with_label( "Wifi Not Prepped" )
        btnPrepare.connect( "clicked", self.btnPrepare )
        self.grid.add(btnPrepare)

        btnStart = Gtk.Button.new_with_label( "Start Attack" )
        btnStart.connect( "clicked", self.btnAttack )
        self.grid.attach_next_to(btnStart, btnPrepare, Gtk.PositionType.RIGHT, 1, 1)

        btnClose = Gtk.Button.new_with_label( "Close" )
        btnClose.connect( "clicked", self.btnClose )
        self.grid.attach_next_to(btnClose, btnStart, Gtk.PositionType.RIGHT, 1, 1)

        #lblTerminal = Gtk.Label()
        self.grid.attach_next_to(self.lblTerminal, btnPrepare, Gtk.PositionType.BOTTOM, 3, 5)

        self.add(self.grid)

        GLib.timeout_add(100, self.update_terminal)

    def non_block_read(self, output):
        fd = output.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        try:
            return output.read().decode("utf-8")
        except:
            return ''

    def update_terminal(self):
        self.lblTerminal.set_text( self.lblTerminal.get_text() + self.non_block_read(self.proc.stdout) )
        return self.proc.poll() is None

    def btnPrepare(self, button):
        if self.prepped:
            button.set_label( "Wifi Not Prepped" )
        else:
            button.set_label( "Wifi Prepped" )
            #systemctl show -p ActiveState --value NetworkManager
            #import subprocess
            #status = subprocess.check_output("systemctl show -p ActiveState --value abc")
            #print(status)
        self.prepped = not self.prepped

    def btnAttack(self, button):
        if self.attacking:
            button.set_label( "Start Attack" )
        else:
            button.set_label( "Stop Attack" )
        self.attacking = not self.attacking

    def btnClose(self, button):
        Gtk.main_quit()

if __name__  == "__main__":
    win = Wifite2UI()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
