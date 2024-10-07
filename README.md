How to run tests?

1. First run server 
2. Click on the link http://127.0.0.1:8000/  you will be redirected to home page

Q 1. Prove that Django signals by default run synchronously

    step 1 - Click on "Sync_Test" Button on Home page
    Answer - In Terminal you will get below Output ---

        synchronization test is running
        creating MyModel instance
        signal received when instance test1 is created
        waiting for signal to finish its job
        signal processing completed
        created MyModel instance
        total time: 4.02 seconds

    Signal got sent after creation of instance in Syncronization_test_view and then post signal got executed

    From total time: 4.02 seconds it proves that time it took to complete our signal operation is also added in total time there for it proves that -------
    -------Django signals by default run synchronously

Q 2. Prove Django signal run in same thread as caller by default.

    step 1. Go back to home page that is http://127.0.0.1:8000/
    step 2. Click on "Thread_Test" button
    step 3. Check Output in terminal 

    Answer - In Terminal you will get below Output---

        threading test is running
        thread of caller : Thread-3 (process_request_thread)
        signal running in a thread : Thread-3 (process_request_thread)

    Here we sent signal form threading_test_view and checked current thread in both caller and receiver and we found that -----
    -----Django signal run in same thread as caller by default-----

Q 3. Prove Django signal run in same database transaction as caller.

    step 1. Go back to home page that is http://127.0.0.1:8000/
    step 2. Click on "Trans_Test" button
    step 3. Check Output in terminal 

    Output--
        transaction test is running
        instance created befor sending signal : created by transaction test
        <QuerySet [<TransModel: TransModel object (1)>]>
        Internal Server Error: /trans_test/

    step 4. Go back to home page that is http://127.0.0.1:8000/
    step 5. Click on "Check_Trans" button
    step 6. Check Output in terminal 

    Output--
        <QuerySet []>

    Answer --

    We created instance in "transaction_test_view" (caller) after creation se sent signal
    to receiver and in receiver we created "intentional error"

    now before error in receiver instance in database got created therefor output of line
        print(f'instance created befor sending signal : {trans.name}')
        print(TransModel.objects.all()) 
    in "transaction_test_view"
    Output
        instance created befor sending signal : created by transaction test
        <QuerySet [<TransModel: TransModel object (1)>]>
    
    After Intentional error output of line 
        print(TransModel.objects.all())

    Output -
        <QuerySet []>

    it proves that whatever operations we performed in caller befor creation of error were called back after creation of error as we used atomic block which perform block of operation as one and any error in whole block transaction will roll back all previous changes as well
    
    This proves that ---
    -----Django signal run in same database transaction as caller-----

Q 4. Cfreatin of rectangle class which reterns an iterable object which gives output after iteration as 
    output-
        Enter Length: 4
        Enter width: 3
        {'length': 4}
        {'width': 3}

    step 1. run python file "class_assignment" in terminal ---- py .\class_assignment.py
    step 2. enter length and width as asked
    step 3. check output

    Answer -- 
        We used "__iter__" and "__next__" methods to get an iterable object of our class


*****************************Thank You***************************************