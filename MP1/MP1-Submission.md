<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Sriniketh Brahmandam (sb2582)</td></tr>
<tr><td> <em>Generated: </em> 10/9/2023 11:32:01 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/sb2582" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.12.37image.png.webp?alt=media&token=f92781c6-5dbc-49b0-a67b-61b20de86de1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for the add_task function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.15.09image.png.webp?alt=media&token=68ffc77d-20c9-472f-9f65-7cd0842cdbf7"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screenshot for adding task successfully  <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.17.03image.png.webp?alt=media&token=1b2f58cc-d911-4a78-93dd-c0d9710f0bb1"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screenshot for rejected task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>In the add_task function we ensures &#39;lastActivity&#39; and set the name, description, and<br>due date<br>Handled due date format in both accepted and rejected cases.<br>Added task lists<br>And<br>enabled to give the feedback to the user and saved the changes.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.30.29image.png.webp?alt=media&token=01527f3b-c55f-4911-818d-181d2e5361be"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screen shot of code for process_update function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>It first check with task index for valid existing tasks, If there was<br>any error it prints Invalid task index and returns, updating that process cannot<br>be proceed.<br><br>If it is valid it will be retrieved and prints the task<br>name.<div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T01.31.38image.png.webp?alt=media&token=33c6a40d-685c-4ebc-9e98-c5e2cc10745e"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the screen shot of the code for update_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T01.19.53image.png.webp?alt=media&token=5dd6faa8-e017-45a6-a5d1-45e4fc1d7380"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is output for successful updating.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>Using update function, I got to know how to updated the tasks that<br>are entered already.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.52.02image.png.webp?alt=media&token=5dc18b88-8db8-444a-9f9e-4bd0345fd4b3"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is code for mark_done function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T01.55.41image.png.webp?alt=media&token=7a03e40e-7e04-48cd-9ab5-6cef39617270"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the output for successful mark_done function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T01.56.26image.png.webp?alt=media&token=a17b48cc-2ace-44b5-9c81-30c33b575c88"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the output for Failure mark_done function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>So in this function it checks the task function whether it was done<br>or not. If the it was done then it will marked as done.<br>If you try to re-do the task than it results in Mark-done already.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.53.24image.png.webp?alt=media&token=2f8d0643-ee38-4870-8293-b484ebc89182"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code for view_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.01.39image.png.webp?alt=media&token=6fa6224e-86c2-4fd4-bceb-acb9b7f32ce2"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the output of successful case.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.03.19image.png.webp?alt=media&token=88130de2-651b-48cb-8e13-4aa27ff89277"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is output of failure case.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.13.16image.png.webp?alt=media&token=461faeb3-336a-40c5-8db9-3fb56e1722f2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Viewing the data that was entered (4 lists)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.55.26image.png.webp?alt=media&token=2a002564-df3c-4ad3-bfa8-2bade491af68"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code for delete_task function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.09.20image.png.webp?alt=media&token=a58ccf5e-dcb0-4866-bac1-81e85d8b5859"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful deletion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.15.09image.png.webp?alt=media&token=aeb142f3-6b85-485a-a83a-440c31a6cda3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deletion invalid <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>So in this task we operate with delete command, by deleting the task<br>that we&#39;re given.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.57.23image.png.webp?alt=media&token=fffd17a8-8482-429c-8240-b2afad9c8128"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code for incomplete_tasks function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.17.27image.png.webp?alt=media&token=48daa187-4144-41c1-94eb-420233e4d765"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tasks that are pending.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.18.59image.png.webp?alt=media&token=7564696c-3535-4db3-9b2c-67c05424e1bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing no tasks pending<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>So in this function we can view the incomplete tasks, and completed tasks<br>which may helpful to check whether all tasks are done.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T00.59.21image.png.webp?alt=media&token=e36b0ed1-7a67-4037-a2e8-39c6bff316f3"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code for get_overdue_tasks function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.22.02image.png.webp?alt=media&token=ee5e3d9e-c88d-4332-be92-24af1dae38a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Resulting no overdue <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.24.27image.png.webp?alt=media&token=b4c6f855-7f9e-4c61-9e3f-351124491703"/></td></tr>
<tr><td> <em>Caption:</em> <p>Overdue was found<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>So, In this function we verify that there was any dew dates were<br>left or the tasks were completed.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T01.00.45image.png.webp?alt=media&token=d959affc-e3c6-408e-aca6-3fb376edccb3"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the code for get_time_remaining function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.32.21image.png.webp?alt=media&token=94db6a42-bdfe-4628-9db8-59b29b0b99fc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful case for remaining function. displaying remaining due time<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.36.16image.png.webp?alt=media&token=66c3e2ee-3572-4f05-8aa7-bcdda938991e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure case. Displaying overdue time<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>So using this function, We can check the due dates of the tasks<br>whether they we&#39;re remained or overdue by using this function.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.41.06image.png.webp?alt=media&token=a901dc79-6e7d-43bb-9dd8-988e256f45c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of the terminal with the output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-10T02.43.53image.png.webp?alt=media&token=0de38e8f-3cda-4d6e-8bd9-bbefc7b55ab8"/></td></tr>
<tr><td> <em>Caption:</em> <p>The data of tasks that are entered.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>So by solving the assignment I learned about how to add, delete, update,<br>checking the tasks and many operations using python language, Had tough time while<br>dealing with the update function for failure cause.&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/16">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/16</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/sb2582" target="_blank">Grading</a></td></tr></table>
