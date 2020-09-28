class LogEvent:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

log_event_list = [
    LogEvent('2020-09-21 12:45:56', 'Login', 'Myworkstation.local', 'Moana'),
    LogEvent('2020-09-22 15:53:42', 'Login', 'Webserver.local', 'Lee'),
    LogEvent('2020-09-21 18:53:21', 'Login', 'Webserver.local', 'Iris'),
    LogEvent('2020-09-22 13:25:34', 'Logout', 'Myworkstation.local', 'Moana'),
    LogEvent('2020-09-21 08:20:01', 'Login', 'Webserver.local', 'Moana'),
    LogEvent('2020-09-23 11:24:35', 'Login', 'Mailserver.local', 'Isa'),
    LogEvent('2020-09-23 12:24:35', 'Login', 'Databaseserver.local', 'Amber'),
    LogEvent('2020-09-23 15:24:35', 'Login', 'Mailserver.local', 'Jude'),
    LogEvent('2020-09-23 11:36:35', 'Login', 'Databaseserver.local', 'Kitty'),
    LogEvent('2020-09-23 16:40:35', 'Logout', 'Mailserver.local', 'Jude'),
    LogEvent('2020-09-25 16:40:35', 'Login', 'Myworkstation.local', 'Ann'),]

def current_users(log_event_list):
    log_event_list.sort(key=lambda log_event: log_event.date)
    on_machines = {}
    for log_event in log_event_list:
        if log_event.machine not in on_machines:
            on_machines[log_event.machine] = set()
        if log_event.type == "Login":
            on_machines[log_event.machine].add(log_event.user)
        elif log_event.type == "Logout":
            on_machines[log_event.machine].remove(log_event.user)
    return on_machines

def logged_out_user(log_event_list):
    log_event_list.sort(key=lambda log_event: log_event.date)
    on_machine = {}
    off_machine = {}
    for log_event in log_event_list:
        if log_event.machine not in on_machine:
            on_machine[log_event.machine] = set()
        elif log_event.machine not in off_machine:
            off_machine[log_event.machine] = set()
        if log_event.type == "Logout":
            off_machine[log_event.machine].add(log_event.user)
        elif log_event.type == "Login":
            on_machine[log_event.machine].add(log_event.user)
    return off_machine


def generate_report_current_users(on_machines):
    for (machine, users) in on_machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("・{}: {}".format(machine, user_list))

def generate_report_logged_out_users(off_machine):
    for (machine, user) in off_machine:
        user_list = ", ".join(users)
        print("・{}: {}".format(machine, user_list))

print("=== CURRENTLY LOGGED IN USERS ===")
current_users = current_users(log_event_list)
generate_report_current_users(current_users)
print("")
print("=== LOGGED OUT USERS===")
logged_out_user = logged_out_user(log_event_list)
generate_report_current_users(logged_out_user)
