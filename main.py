#!/usr/bin/python
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

        hbox = Gtk.Box( spacing=6 )
        self.add(hbox)

        # add buttons
        button = Gtk.Button.new_with_label( "Wifi Not Prepped" )
        button.connect( "clicked", self.btnPrepare )
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic( "Start Attack" )
        button.connect( "clicked", self.btnAttack )
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic( "_Close" )
        button.connect( "clicked", self.btnClose )
        hbox.pack_start(button, True, True, 0)

        # add terminal
        cli = Gtk.TextView()
        scroll = Gtk.ScrolledWindow()
        scroll.add( cli )
        hbox.pack_start( scroll, True, True, 0 )

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
            button.set_label( "Stop Attack" )
        else:
            button.set_label( "Start Attack" )
        self.attacking = not self.attacking

    def btnClose(self, button):
        Gtk.main_quit()

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()