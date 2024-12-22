import { Navigation } from './sidenav.model';

export const NAVIGATION_ITEMS: Navigation[] = [
  {
    label: 'Home',
    id: 'home',
    path: '',
    active: false,
    icon: 'home',
  },
  {
    label: 'Income',
    id: 'income',
    path: 'income',
    active: false,
    icon: 'attach_money',
  },
  {
    label: 'Expense',
    id: 'expense',
    path: 'expense',
    active: false,
    icon: 'money_off',
  },
  {
    label: 'Budget',
    id: 'budget',
    path: 'budget',
    active: false,
    icon: 'account_balance_wallet',
  },
  {
    label: 'Goal',
    id: 'goal',
    path: 'goal',
    active: false,
    icon: 'flag',
  },
  {
    label: 'Report',
    id: 'report',
    path: 'report',
    active: false,
    icon: 'bar_chart',
  },
];
