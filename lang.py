def get_language_dict(language: str):
    return {
        "English": {
            "risk_tab": "Risk Calculator",
            "journal_tab": "Trade Journal",
            "performance_tab": "Performance",
            "app_title": "Jetset Trading Pro+",
            "date": "Date", "time": "Time", "ticker": "Ticker", "type": "Type", "buy": "Buy", "sell": "Sell",
            "entry": "Entry Price", "stop": "Stop Loss", "tp1": "Take Profit 1", "tp2": "Take Profit 2", "exit": "Exit Price",
            "qty": "Quantity", "fees": "Fees", "strategy": "Strategy", "notes": "Notes", "upload": "Upload Screenshot",
            "save": "💾 Save Trade", "tag": "Tag", "sentiment": "Sentiment", "suggested_qty": "Suggested Quantity:",
            "calculate": "Calculate", "risk_pct": "Risk % per Trade", "capital": "Account Capital",
            "leverage": "Leverage", "asset_type": "Asset Type",
            "set_exit": "✅ Set Exit", "update_exit": "Set Exit Price", "filter_ticker": "Filter by Ticker",
            "filter_date": "Filter by Date", "stats": "Stats", "total_trades": "Total Trades", "wins": "Wins", "losses": "Losses",
            "win_rate": "Win Rate", "avg_rr": "Avg R:R", "expectancy": "Expectancy", "drawdown": "Max Drawdown",
            "win_pie": "Win/Loss Ratio", "equity_curve": "Equity Curve", "monthly": "Monthly P&L",
            "top_trades": "Top Trades", "import": "Import Excel", "export": "Export Excel",
            "no_data": "No trades to analyze.", "risk_error": "Stop Loss must be different from Entry",
            "edit_trade": "✏️ Edit Trade", "delete_trade": "🗑️ Delete Trade", "confirm_delete": "❌ Confirm Delete",
            "reset_trades": "🔄 Reset All Trades"
        },
        "Français": {
            "risk_tab": "Calculateur de Risque",
            "journal_tab": "Journal de Trading",
            "performance_tab": "Performance",
            "app_title": "Jetset Trading Pro+",
            "date": "Date", "time": "Heure", "ticker": "Symbole", "type": "Type", "buy": "Achat", "sell": "Vente",
            "entry": "Prix d'entrée", "stop": "Stop Loss", "tp1": "Take Profit 1", "tp2": "Take Profit 2", "exit": "Prix de sortie",
            "qty": "Quantité", "fees": "Frais", "strategy": "Stratégie", "notes": "Notes", "upload": "Capture graphique",
            "save": "💾 Enregistrer", "tag": "Étiquette", "sentiment": "Sentiment", "suggested_qty": "Quantité suggérée :",
            "calculate": "Calculer", "risk_pct": "% de Risque", "capital": "Capital du compte",
            "leverage": "Effet de levier", "asset_type": "Type d'actif",
            "set_exit": "✅ Clôturer", "update_exit": "Clôturer un trade", "filter_ticker": "Filtrer par symbole",
            "filter_date": "Filtrer par date", "stats": "Statistiques", "total_trades": "Total des trades", "wins": "Trades gagnants",
            "losses": "Trades perdants", "win_rate": "Taux de réussite", "avg_rr": "Moyenne R:R", "expectancy": "Espérance",
            "drawdown": "Drawdown Max", "win_pie": "Ratio Gain/Perte", "equity_curve": "Courbe de Capital", "monthly": "P&L mensuel",
            "top_trades": "Top Trades", "import": "Importer Excel", "export": "Exporter Excel",
            "no_data": "Aucun trade à analyser.", "risk_error": "Stop Loss doit être différent du prix d'entrée",
            "edit_trade": "✏️ Modifier Trade", "delete_trade": "🗑️ Supprimer Trade", "confirm_delete": "❌ Confirmer Suppression",
            "reset_trades": "🔄 Réinitialiser tous les trades"
        }
    }[language]
