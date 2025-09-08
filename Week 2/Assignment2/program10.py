class BugTracker:

    def __init__(self, bugs):
        self.bugs = bugs

    def add_bug(self, description, severity):
        self.bugs[str(int(list(self.bugs.keys())[-1])+1)] = {"description" : description, "severity" : severity, "status" : "Open"}

    def update_status(self, bug_id, new_status):
        for id, bug_details in self.bugs.items():
            if (id == bug_id):
                bug_details["status"] = new_status
            self.bugs[id] = bug_details


    def list_all_bugs(self):
        for key,value in self.bugs.items():
            print(key,":", value)
        print()


if __name__ == "__main__":
    bugs = BugTracker({
        "1": {"description": "Issue1", "severity": "High","status": "Open" },
        "2": {"description": "Issue2", "severity": "Medium", "status": "In Progress"},
        "3": {"description": "Issue3", "severity": "Low", "status": "Open"}
    })
    bugs.list_all_bugs()
    bugs.add_bug("Issue4","Low")
    bugs.list_all_bugs()
    bugs.update_status("2","Closed")
    bugs.list_all_bugs()
    bugs.add_bug("Issue5", "High")
    bugs.list_all_bugs()




