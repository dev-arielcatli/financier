import { Navigation } from './sidenav.model';

export const NAVIGATION_ITEMS: Navigation[] = [
  {
    label: 'Home',
    id: 'home',
    path: '',
    active: false,
    icon: 'home',
    disabled: true,
  },
  {
    label: 'Income',
    id: 'income',
    path: 'income',
    active: false,
    icon: 'attach_money',
    disabled: false,
  },
  {
    label: 'Expense',
    id: 'expense',
    path: 'expense',
    active: false,
    icon: 'money_off',
    disabled: false,
  },
  {
    label: 'Budget',
    id: 'budget',
    path: 'budget',
    active: false,
    icon: 'account_balance_wallet',
    disabled: true,
  },
  {
    label: 'Goal',
    id: 'goal',
    path: 'goal',
    active: false,
    icon: 'flag',
    disabled: true,
  },
  {
    label: 'Report',
    id: 'report',
    path: 'report',
    active: false,
    icon: 'bar_chart',
    disabled: true,
  },
];
