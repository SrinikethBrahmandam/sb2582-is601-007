<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Sriniketh Brahmandam (sb2582)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 3:30:19 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sb2582" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.19.17image.png.webp?alt=media&token=71c69984-0017-4d89-b96c-14e05acefd72"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login into the page with credentials <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.24.30image.png.webp?alt=media&token=ee8da8ea-1ab7-4477-be1c-b7bc70604a44"/></td></tr>
<tr><td> <em>Caption:</em> <p>The given username is taken. So can&#39;t register again with same username.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.26.27image.png.webp?alt=media&token=d75d2fb0-8ec1-4eda-94ee-14c9a02325b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>The email was already registered with different username, So it&#39;s not available to<br>register again.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.31.26image.png.webp?alt=media&token=afae5e60-e720-41bd-b2b0-49660cfd8ce6"/></td></tr>
<tr><td> <em>Caption:</em> <p>There should be minimum 8 characters for password, If not it pop a<br>message box with there should be at least 8 characters to create a<br>password.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.35.03image.png.webp?alt=media&token=bebb2211-86a6-43c3-ab23-e10f938b660f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password, When we entered the wrong password.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.36.53image.png.webp?alt=media&token=f5f9d382-a88b-4a91-a01a-beca7230926c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid user, Because the credentials given were of wrong email that haven&#39;t been<br>registered yet.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T07.39.49image.png.webp?alt=media&token=36e279b1-3d0c-42a4-be94-3a21024fce42"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database view of the users who enrolled for the web application<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>Form Handling:</div><div>Forms are created using the Flask-WTF extension and WTForms library. Forms are<br>used for user registration, login, and profile updates.</div><div><br></div><div>Validation Logic:</div><div>Validation logic is defined using<br>validators provided by WTForms. Custom validation functions ('validate_username' and 'validate_email') are used for<br>specific validation requirements. Errors are handled by raising 'ValidationError' when validation fails.</div><div><br></div><div>Password Handling:</div><div>Passwords<br>are handled using the 'PasswordField' from WTForms. Password confirmation is enforced through the<br>'EqualTo' validator.</div><div><br></div><div><br></div><div>Database Utilization:</div><div>User registration data (email, username, hashed password) is stored in the<br>'IS601_Users' table.&nbsp;</div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T18.57.16image.png.webp?alt=media&token=bb091ad7-ebc1-418c-836c-5979d2eebdd9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tried to login with non-existing user.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T18.58.29image.png.webp?alt=media&token=6f5cb208-17fb-409b-9a40-cc8a76514ee2"/></td></tr>
<tr><td> <em>Caption:</em> <p>The password was mismatched because we entered wrong credentials.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T18.59.57image.png.webp?alt=media&token=6a88e8a0-a569-44b5-9069-383d9060c8f2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The &#39;RegisterForm&#39; is used for user registration. This form includes fields for username,<br>email, password, and password confirmation.Upon successful validation, The &#39;LoginForm&#39; is used for user<br>login.The form includes fields for email or username and password.<br><br><div>The &#39;validate_username&#39; function checks<br>the chosen username&#39;s format and availability.</div><div>The &#39;validate_email&#39; function checks if the entered value<br>is a valid email address or username.<br><br>Passwords are hashed and verified using Flask-Bcrypt<br>before storing them&nbsp; in the database and then during the login process.<br><br><div>User credentials<br>(email or username and password) are retrieved from the &#39;IS601_Users&#39; table for authentication.<br>Email and username changes are updated in the &#39;IS601_Users&#39; table. Password changes involve<br>verifying the current password and updating the hashed password in the database.</div><div><br></div><br><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.09.53image.png.webp?alt=media&token=ea1ed27e-e5d7-427d-a215-c04c283d09a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully logged out <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.17.08image.png.webp?alt=media&token=e36e2b8c-eeeb-4bd9-9d7a-7a3120f44d28"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized for user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><font color="#374151" face="Söhne, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans,<br>sans-serif, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol,<br>Noto Color Emoji"><span style="font-size: 16px; white-space-collapse: preserve;">&nbsp;Flask-Login provides a convenient way to manage<br>user sessions, and Flask-Principal is used to manage roles and identity changes. The<br>session stores information about the current user, and proper notification mechanisms ensure a<br>seamless integration of login and logout processes.</span></font><br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.33.01image.png.webp?alt=media&token=ce1bd4b8-9e99-4450-b608-69cb3e5b4601"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.33.14image.png.webp?alt=media&token=316fa1ca-e4fc-4e90-9803-cc40c1708b92"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission denied <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.35.29image.png.webp?alt=media&token=749d4c8a-1138-40b1-891a-7c5d3d0a5b94"/></td></tr>
<tr><td> <em>Caption:</em> <p>View of Roles table in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.37.09image.png.webp?alt=media&token=0283960b-7c0c-43b3-a0c5-32b617dfd9b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>View of Userroles table in Database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>The &#39;@login_required&#39; decorator is used to protect routes, ensuring that only authenticated users<br>can access certain pages. Flask-Login handles the session management, redirects to the login<br>page when needed, and provides access to the current user object within protected<br>routes.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>role-protected pages involve defining roles and permissions, using decorators to protect routes, assigning<br>roles to users upon login, and implementing access control in templates. Flask-Principal facilitates<br>the integration of role-based access control in Flask applications.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.44.44image.png.webp?alt=media&token=47c1c4aa-ee4c-4625-b894-fb44b09a04e3"/></td></tr>
<tr><td> <em>Caption:</em> <p>List of samples that are entered<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.45.08image.png.webp?alt=media&token=28401249-5de8-4860-8cff-d1e421a05d5b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile page for updation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>&#39;RoleForm&#39; in a Flask web application, This form is designed to gather information<br>related to user roles. It includes fields for the role name, description, and<br>an &quot;Is Active&quot; checkbox. Validators are applied to enforce data requirements. The form<br>can be used to render HTML forms for creating or editing user roles<br>in Flask routes. the use of Flask-WTF and WTForms for form creation and<br>validation of a Flask application.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.56.12image.png.webp?alt=media&token=b0e712b0-ecb6-44b1-83c1-e45a5f577b45"/></td></tr>
<tr><td> <em>Caption:</em> <p>The username trying to enroll was already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.57.21image.png.webp?alt=media&token=00f4f418-ed9d-48ec-9333-d96b65b4577b"/></td></tr>
<tr><td> <em>Caption:</em> <p>The email trying to enroll was already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T19.58.28image.png.webp?alt=media&token=4000d5b6-596d-4b51-9063-d870c64c27a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>The password entered was wrong<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>To make messages more user-friendly, the code employs the Flask &#39;flash&#39; function to<br>generate flash messages. These messages are short, concise, and provide information about the<br>success or failure of user actions. For example, in the authentication routes (&#39;login&#39;,<br>&#39;register&#39;, &#39;logout&#39;, and &#39;profile&#39;), flash messages are used to inform users about the<br>outcome of their actions, such as successful login, registration, or errors like invalid<br>passwords. The messages are categorized by their importance and colored for emphasis (e.g.,<br>success messages in green, warnings in yellow, and errors in red). This approach<br>enhances user experience by delivering clear and contextual messages, making it easier for<br>users to understand the outcome of their interactions with the application.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T20.02.54image.png.webp?alt=media&token=7a507275-1963-4c32-a57b-ed1f39e7d2e1"/></td></tr>
<tr><td> <em>Caption:</em> <p>User details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The <code>/profile</code> route in the Flask application involves retrieving the authenticated user&#39;s data<br>from the database and displaying it in the <code>ProfileForm</code>. This process ensures that<br>users see their current profile information when accessing the profile page, enhancing the<br>personalized experience.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T20.11.45image.png.webp?alt=media&token=fe624c99-d40e-4092-a755-f4c7a70842f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username was already existed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T20.14.40image.png.webp?alt=media&token=8d96bec2-e981-49b3-9c4b-45dec6c629fd"/></td></tr>
<tr><td> <em>Caption:</em> <p>email was already existed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T20.17.45image.png.webp?alt=media&token=f7c154d3-1140-4d8a-bc61-9ba58a8e0e43"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mis matched<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T20.16.55image.png.webp?alt=media&token=d0ff23fb-7abd-4dfe-bf07-dd3e11df7602"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database view before updating<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-12-14T20.22.20image.png.webp?alt=media&token=af776a4c-1945-4b0f-8a9b-6f4d5652e2d3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database view after updating <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The <code>/profile</code> route in the Flask application handles the editing process when users<br>update their profile information. The logic involves validating the form data, including email,<br>username, and password fields, and then making corresponding updates to the database. Custom<br>validation ensures that password changes are securely processed. This ensures that user modifications<br>are properly validated and updated in the database, enhancing the overall security and<br>integrity of user profile data.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>During this milestone, one notable issue was the absence of required Python packages,<br>leading to multiple &quot;ModuleNotFoundError&quot; exceptions. These missing modules were identified and resolved by<br>installing the required packages using the <code>pip</code> command.<br><br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sb2582-prod-6b6e53619b9b.herokuapp.com/login">https://is601-sb2582-prod-6b6e53619b9b.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<<<<<<< HEAD
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sb2582" target="_blank">Grading</a></td></tr></table>
=======
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sb2582" target="_blank">Grading</a></td></tr></table>
>>>>>>> 5f51622e2190c2dc29919296c18ec62a3472cbbf
