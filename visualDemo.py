from psychopy import visual, core, event

win = visual.Window([400,400])
txt = visual.TextStim(win, text='hello')
txt.draw()
win.flip()
core.wait(2)

