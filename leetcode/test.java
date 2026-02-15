class WithdrawalController {
    private final NotificationService notifier = new NotificationService();
    private final AuditLogger logger = AuditLogger.getInstance();

    void submitRequest(WithdrawalRequest req){
        req.submit();
        notifier.notifyAll("New withdrawal request submitted!");
        logger.logAction("Withdrawal submitted: " + req.getRequestId());
    }
}
