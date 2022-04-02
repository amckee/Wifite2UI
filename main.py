#!/usr/bin/python3
import gi
from subprocess import Popen, PIPE

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ButtonWindow( Gtk.Window ):
    prepped = False
    attacking = False

    def __init__(self):
        super().__init__( title="Wifite2 UI" )
        self.set_border_width( 10 )

        #box = Gtk.Box( spacing=6 )
        #self.add(box)
        grid = Gtk.Grid()

        # add buttons
        btnPrepare = Gtk.Button.new_with_label( "Wifi Not Prepped" )
        btnPrepare.connect( "clicked", self.btnPrepare )
        grid.add(btnPrepare)
        #box.pack_start( button, True, True, 0 )

        btnStart = Gtk.Button.new_with_label( "Start Attack" )
        btnStart.connect( "clicked", self.btnAttack )
        grid.attach_next_to(btnStart, btnPrepare, Gtk.PositionType.RIGHT, 2, 2)
        #box.pack_start( button, True, True, 0 )

        btnClose = Gtk.Button.new_with_label( "Close" )
        btnClose.connect( "clicked", self.btnClose )
        grid.attach_next_to(btnClose, btnStart, Gtk.PositionType.RIGHT, 1, 1)
        #box.pack_start( button, True, True, 0 )

        # add terminal
        #cli = Gtk.TextView()
        #scroll = Gtk.ScrolledWindow()
        #scroll.add( cli )
        #grid.attach_next_to(btnPrepare, cli, Gtk.PositionType.BOTTOM, 1, 1)
        #box.pack_start( scroll, True, True, 0 )

        self.add(grid)

        proc = Popen("ping -c10 localhost", stdout=PIPE, shell=True)
        sub_outp = ""
    
    def non_block_read(output):
        fd = output.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        try:
            return output.read().decode("utf-8")
        except:
            return ''

    def cli_update():
        self.hbox.cli.get_buffer().insert_at_cursor(non_block_read(sub_proc.stdout))
        return self.sub_proc.poll() is None

    def btnPrepare(self, button):
        if self.prepped:
            button.set_label( "Wifi Not Prepped" )
        else:
            button.set_label( "Wifi Prepped" )
        self.prepped = not self.prepped

    def btnAttack(self, button):
        if self.attacking:
            button.set_label( "Start Attack" )
        else:
            button.set_label( "Stop Attack" )
        self.attacking = not self.attacking

    def btnClose(self, button):
        Gtk.main_quit()

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()