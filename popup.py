parent_h = chrome.current_window_handle
handles = chrome.window_handles
handles.remove(parent_h)
chrome.switch_to.window(handles.pop())

...

chrome.execute_script("window.close()")
chrome.switch_to.window(parent_h)
