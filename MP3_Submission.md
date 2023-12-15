<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Sriniketh Brahmandam (sb2582)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 9:34:04 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/sb2582" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T21.59.10image.png.webp?alt=media&token=ed43c5cc-3c31-447c-b539-6c13c9ef8852"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code view of Index.html<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.01.31image.png.webp?alt=media&token=42ed8685-0cdb-4677-8797-c3336ce0ea0c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code view of nav.html<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.05.59image.png.webp?alt=media&token=e55870b5-05b0-41e5-9649-9aa3cbf80d1b"/></td></tr>
<tr><td> <em>Caption:</em> <p>check that it&#39;s a .csv file, return a proper flash message if it&#39;s<br>not and don&#39;t attempt to process the file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.07.39image.png.webp?alt=media&token=98ad123d-cb9d-456f-ac0c-ca4460b58a67"/></td></tr>
<tr><td> <em>Caption:</em> <p>read the csv file stream as a dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.08.12image.png.webp?alt=media&token=989ce4ca-763d-42ec-b4ad-8f4f25e420f1"/></td></tr>
<tr><td> <em>Caption:</em> <p>extract organization data and append to organization list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.09.09image.png.webp?alt=media&token=8fbb12e0-8864-4e28-b14a-6a330a9e95cf"/></td></tr>
<tr><td> <em>Caption:</em> <p>extract donation data and append to donation list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.11.38image.png.webp?alt=media&token=fd6f40c8-55c3-4500-8127-d5207c234157"/></td></tr>
<tr><td> <em>Caption:</em> <p>display flash message about number of organizations inserted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.12.31image.png.webp?alt=media&token=5c47b4f8-9d8a-48d6-892f-c25aed54fe41"/></td></tr>
<tr><td> <em>Caption:</em> <p>display flash message (info) that no organizations were loaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.13.27image.png.webp?alt=media&token=7091f489-77d6-4cc0-8750-1d18ae8efc7f"/></td></tr>
<tr><td> <em>Caption:</em> <p>display flash message about number of donations loaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T22.14.32image.png.webp?alt=media&token=2118a0a6-ea95-4b94-9a5e-fe5fbcc76f9d"/></td></tr>
<tr><td> <em>Caption:</em> <p>display flash message (info) that no donations were loaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.56.30image.png.webp?alt=media&token=bda9b6e9-116a-4110-ac70-1fae18bfd6c7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website view for edit Donation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.55.27image.png.webp?alt=media&token=b3995dd8-4d5f-414e-af5f-5c87e71ef4de"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website view for Creating an donation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.15.39image.png.webp?alt=media&token=94444df2-1043-43c6-b591-9b9e64d90d17"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website view for Search in donations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.19.34image.png.webp?alt=media&token=d0412378-092a-4ad4-af00-96bb0e505013"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.21.33image.png.webp?alt=media&token=879e5afd-18df-4184-a3f7-55e05b28ff55"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.21.53image.png.webp?alt=media&token=7954dd2b-d60b-4f42-a479-55b50ac09a63"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.22.14image.png.webp?alt=media&token=1190b236-3735-4920-9ed6-d487df44f6fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.22.26image.png.webp?alt=media&token=9e6e2159-0346-4b52-b5ef-9b6799a66e7a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.24.01image.png.webp?alt=media&token=a56efeca-b9cf-4000-b43d-bd16ad148d3a"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot 6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.27.40image.png.webp?alt=media&token=6f22d143-4ef0-43fb-9e55-321dac28a0c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot 7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.28.00image.png.webp?alt=media&token=d3cd7ca4-9971-401d-8b4e-e0b276cce40b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.28.15image.png.webp?alt=media&token=25a43713-430c-4d1a-bd51-1e2b0f7469e7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.28.52image.png.webp?alt=media&token=02c017af-c4d6-46f1-ac3d-25fa471d9dd8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.29.21image.png.webp?alt=media&token=49840940-ac25-4f5d-81d5-24dbf796dffd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.29.36image.png.webp?alt=media&token=34ac3c04-10e5-4843-9615-87b5e6b7d14f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 12<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.33.33image.png.webp?alt=media&token=f8a21764-d7d1-427b-b43d-4f124c10b424"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.34.35image.png.webp?alt=media&token=bb259465-f279-4737-9f96-32c9a2338d5f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.36.42image.png.webp?alt=media&token=8938019b-d047-4d36-abdc-ac7963cf6ff8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.37.52image.png.webp?alt=media&token=670e2639-2aeb-4b8b-9f5e-f9d1105a6e35"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.38.43image.png.webp?alt=media&token=c1a574b0-0f44-47e4-b025-ea240b755638"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.41.35image.png.webp?alt=media&token=8647d58e-fd1f-445b-932b-080e1833d55f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.43.09image.png.webp?alt=media&token=051c66eb-ed8e-4b31-a23c-a46d6550ce78"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.44.25image.png.webp?alt=media&token=11009db7-8199-4c67-a320-db056ab38d2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.47.29image.png.webp?alt=media&token=e98d070b-47e9-4c55-9ba6-109f35081a33"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.49.00image.png.webp?alt=media&token=0a2515a8-a003-49ea-9fa8-62aae167079d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.13.04image.png.webp?alt=media&token=2df983bc-35ca-401e-ac5b-fe999ce111c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T00.58.17image.png.webp?alt=media&token=7fe1fb29-43fd-42b8-a962-bfb873961472"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website view of Create organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.00.14image.png.webp?alt=media&token=48c5f8fd-becc-43d6-8db3-13c4cb419400"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website view of edit organization<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.02.04image.png.webp?alt=media&token=cca4850f-1272-40e1-a072-dc405fdfe8c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.05.50image.png.webp?alt=media&token=b32c71b2-c680-4023-a347-eb7b781f48d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.09.13image.png.webp?alt=media&token=92921ba0-31a1-4342-8698-295f13609f89"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.10.23image.png.webp?alt=media&token=ca298f81-ac55-414b-847d-417fbbcba80b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.11.59image.png.webp?alt=media&token=3af1d569-c57e-476a-9af7-9bc65f0f5ed1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.14.07image.png.webp?alt=media&token=31b08634-0773-4235-9980-c4744cc7981a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T02.30.18image.png.webp?alt=media&token=48176d40-f8ee-48f6-b400-3a43f01c5c2f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.16.49image.png.webp?alt=media&token=a6b902b3-5da7-4618-bb92-91be025b92fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.19.04image.png.webp?alt=media&token=3fcb6482-7be0-4af5-bea3-08a1d993f9c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.20.08image.png.webp?alt=media&token=2c2f18c7-5d2e-445d-94cc-f6470967fec2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.21.11image.png.webp?alt=media&token=24d8952f-5db3-454c-8c1f-078af9664cd5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.22.18image.png.webp?alt=media&token=97d9dc7f-476c-484f-84c4-16000f4cdfa3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.23.34image.png.webp?alt=media&token=0e8956ef-1ad3-439f-a15f-8d4629f4e4ed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot 1<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.45.44image.png.webp?alt=media&token=69ed0050-fe5c-4bc3-91bf-8166f35c0566"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the passing testcases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.47.23image.png.webp?alt=media&token=e0c9b53c-90f9-42fc-be26-a902249c01bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test_organizations.py testcases that are successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.49.14image.png.webp?alt=media&token=beb3bbe6-7b60-43e9-9ee3-5bca9a1c13c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the test_upload.py test case that was successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T01.50.35image.png.webp?alt=media&token=700030e9-af04-4fde-aea9-63ffbce93f83"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test_index.py test case that was successsful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>Yes, All the test cases are successfully passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/40">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/40</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T02.23.08image.png.webp?alt=media&token=ce142507-2c29-4dec-842d-f5f7e499717b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the github commit history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-15T02.14.26image.png.webp?alt=media&token=91c02817-5aeb-48de-945c-7c47debce5d8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the wakatime dashboard<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="http://127.0.0.1:8080/">http://127.0.0.1:8080/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/sb2582" target="_blank">Grading</a></td></tr></table>
