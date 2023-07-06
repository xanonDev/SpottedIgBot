const persistedData = JSON.parse(localStorage.getItem('reduxPersist:__app__'));

if (persistedData && persistedData.accounts) {
    for (const accountId in persistedData.accounts) {
        if (persistedData.accounts.hasOwnProperty(accountId)) {
            const account = persistedData.accounts[accountId];
            if (account.hasOwnProperty('accessToken')) {
                const accessToken = account.accessToken;
                console.log(accessToken);
            }
        }
    }
}