<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Sriniketh Brahmandam (sb2582)</td></tr>
<tr><td> <em>Generated: </em> 10/26/2023 7:13:47 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/sb2582" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T20.14.10WhatsApp%20Image%202023-10-26%20at%2015.22.51_58129525.jpg.webp?alt=media&token=b092b8c4-2b9b-4ef5-8946-b5ff52dcfac8"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screen shot we have run the code and gave input for<br>pumpkin machine.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T20.15.56image.png.webp?alt=media&token=0919e901-3551-4345-be4e-9f49290322f9"/></td></tr>
<tr><td> <em>Caption:</em> <p>This part of code refers to how calculate_cost function works<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>The <code>run</code> method sequentially guides users through PumpkinMachine stages. It adapts prompts and<br>options based on the current stage. Users select pumpkins, stencils, extras, or make<br>payments. It gracefully manages exceptions like stock shortages, cleaning needs, and invalid choices.<br>If users opt to quit, the program ends; otherwise, it proceeds through pumpkin<br>creation.<br><br>The total cost is presented to the user with currency formatting. The line<br>&quot;Your total is {expected:.2f}, please enter the exact value.&quot; utilizes f-strings to format<br>the expected amount as a floating-point number with precisely two decimal digits (:.2f).<br>This formatting guarantees that the total cost is visibly displayed in a currency<br>format with two decimal places, ensuring clarity for the user.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T20.38.32image.png.webp?alt=media&token=08bc673b-61b8-40cf-b411-9677991bf2fd"/></td></tr>
<tr><td> <em>Caption:</em> <p>This part of the code is where exceptions was handled. (Part 1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T20.41.04image.png.webp?alt=media&token=a541ea07-5625-4e2b-89d4-664fe50c690a"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this part of we included NeedsCleaningException, InvalidChoiceException, ExceededRemainingChoicesException, InvalidPaymentException. (Part 2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>Here we are gonna see 5 exception handlings.<br>1) Out of stock Exception: When<br>an item is out of stock in the current stage. This exception will<br>be raised.&nbsp;The exception message is printed, informing the user of the specific stage<br>where the item is out of stock.<br>2)NeedsCleaningException : When the machine needs cleaning,<br>the code raises a NeedsCleaningException. The user is prompted to type &#39;clean&#39; to<br>clean the machine; other words are ignored. A message confirms whether or not<br>the machine was cleaned.&nbsp;<div>3)&nbsp;InvalidChoiceException Handling: If the user makes an invalid choice, the<br>code raises an InvalidChoiceException for the specific stage. The program prints an error<br>message indicating that the choice was invalid in the current stage and allows<br>the user to make another selection.</div><div>4)&nbsp;ExceededRemainingChoicesException Handling: When the user exceeds the allowed<br>number of choices in a category, the code raises an ExceededRemainingChoicesException. The program<br>prints an error message specifying the stage where the choice limit was exceeded<br>and automatically moves the user to the next stage.</div><div>5)&nbsp;InvalidPaymentException Handling: In the Payment<br>stage, if the entered payment is invalid, the code raises an InvalidPaymentException. The<br>program prints an error message indicating that the payment was invalid and allows<br>the user to retry the payment.</div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.14.46image.png.webp?alt=media&token=ec1dcef4-513e-46e1-a968-ba5b1c535e9e"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test case ensures that selecting a pumpkin is the first valid step<br>and raises an InvalidStageException when trying to choose a face stencil or extra<br>before selecting a pumpkin. It then verifies that the pumpkin selected is &quot;Mini<br>Pumpkin.&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.18.36image.png.webp?alt=media&token=d8168a96-7b7e-4a7e-b4c5-3e998a4fb2e9"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test case checks if the &quot;OutOfStockException&quot; is raised when trying to select<br>a face stencil that is out of stock. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.32.05image.png.webp?alt=media&token=bdd1bc8b-fca9-4999-abc1-93e2d50ae8d4"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test case verifies if the &quot;OutOfStockException&quot; is raised when attempting to select<br>an extra that is out of stock.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.38.10image.png.webp?alt=media&token=6f1e84a6-6400-477e-80a9-0abdea33eee4"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test case ensures that an &quot;ExceededRemainingChoicesException&quot; is raised when attempting to select<br>more than the allowed three face stencils for a pumpkin, specifically by choosing<br>a fourth face stencil<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.41.13image.png.webp?alt=media&token=1d58311e-a7ad-419d-84c6-66ab28c64862"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test case  is raised when attempting to select more than the<br>allowed three extras for a pumpkin, specifically by choosing a fourth extra.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.44.13image.png.webp?alt=media&token=d6275f70-ea58-4ed0-af87-254b2c36dfb9"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test case ensures that the &quot;total_products&quot; variable increments correctly when a valid<br>purchase is made including selecting a pumpkin, face stencil, extras, and completing the<br>payment process.<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.46.11image.png.webp?alt=media&token=cb6fcc56-0543-4cfd-8995-aae18adf128a"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test verifies that the &quot;clean_machine&quot; method properly resets the &quot;remaining_uses&quot; variable to<br>its initial value when called.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T21.48.04image.png.webp?alt=media&token=5030fb57-23b9-4125-99df-caff4cdeb669"/></td></tr>
<tr><td> <em>Caption:</em> <p>This test ensures that the &quot;reset&quot; method correctly clears the &quot;inprogress_pumpkin&quot; list, resulting<br>in an empty list after calling the reset method.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>This test checks that selecting a pumpkin is the first valid step. It<br>verifies that attempting to choose a face stencil or extra before selecting a<br>pumpkin raises an InvalidStageException. Afterward, it ensures that the pumpkin selected is &quot;Mini<br>Pumpkin.&quot;<div><br></div><div>It depletes the stock of a specific face stencil (&quot;Happy Face&quot;) and then<br>tries to choose it after selecting a pumpkin. The test checks that an<br>OutOfStockException is raised when trying to select an out-of-stock face stencil.<br></div><div><br></div><div><div>Similar to the<br>second test, but it depletes the stock of a specific extra (&quot;LED Candle&quot;)<br>and then tries to choose it after selecting a pumpkin and advancing to<br>the extras stage. It checks that an OutOfStockException is raised in this case.</div></div><div><br></div><div>This<br>test ensures that the system can handle choosing up to three face stencils<br>correctly. It selects three face stencils in any combination and then attempts to<br>add a fourth face stencil. The test confirms that an ExceededRemainingChoicesException is raised<br>as expected.<br></div><div><br></div><div>Similar to the fourth test but focuses on choosing up to three<br>extras. It adds three extras in any combination and then attempts to add<br>a fourth extra, which should raise an ExceededRemainingChoicesException.<br></div><div><br></div><div>This test checks the increment of<br>the &quot;total_products&quot; variable when a valid purchase is made, including selecting a pumpkin,<br>a face stencil, extras, and completing the payment process.<br></div><div><br></div><div>This test ensures that the<br>&quot;reset&quot; method clears the &quot;inprogress_pumpkin&quot; list, making it empty after calling the reset<br>method.&nbsp;<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/27">https://github.com/SrinikethBrahmandam/sb2582-is601-007/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I faced little error while running the test cases. Apart from that everything<br>went smoother.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T22.01.57WhatsApp%20Image%202023-10-26%20at%2015.22.51_0038bfc0.jpg.webp?alt=media&token=585d940d-d4ce-44ae-af33-4eabe5e68300"/></td></tr>
<tr><td> <em>Caption:</em> <p>Scerrenshots of output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2582%2F2023-10-26T22.05.58image.png.webp?alt=media&token=368a6161-73ed-4590-87b4-a2cf783f8990"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshots of output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/sb2582" target="_blank">Grading</a></td></tr></table>
