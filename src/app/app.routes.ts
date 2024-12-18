import { Routes } from '@angular/router';
import { ExpenseComponent } from './pages/expense/expense.component';
import { IncomeComponent } from './pages/income/income.component';
import { BudgetComponent } from './pages/budget/budget.component';
import { GoalComponent } from './pages/goal/goal.component';
import { AiComponent } from './pages/ai/ai.component';

export const routes: Routes = [
  {
    path: 'expense',
    component: ExpenseComponent,
  },
  { path: 'income', component: IncomeComponent },
  { path: 'budget', component: BudgetComponent },
  { path: 'goal', component: GoalComponent },
  { path: 'ai', component: AiComponent },
  { path: '', redirectTo: '/expense', pathMatch: 'full' },
];
